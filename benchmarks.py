#!/usr/bin/env python

import glob
import os
import re
import sys
from shutil import copy
from subprocess import check_output, CalledProcessError

from config import LogFiles, TempDir, PLANNER_BENCHMARKS_DIR, SCRIPT_DIR, RESULT_OUTPUT, VAL_PATH, CONFIG_TEMPORAL_DOMAINS, Configuration
from singularity import run_image

from results import BenchmarkResult

class Benchmark(object):
    def __init__(self, folder, domain, problem, domain_path=None, problem_path=None,
                 optimal_plan_cost_lower_bound=None, optimal_plan_cost_upper_bound=None, cost_bound=2147483647):
        self.folder = folder.strip()
        self.domain = domain.strip()
        self.problem = problem.strip()
        self.domain_path = os.path.join(PLANNER_BENCHMARKS_DIR, domain_path.strip(), self.folder, self.domain)
        self.problem_path = os.path.join(PLANNER_BENCHMARKS_DIR, problem_path.strip(), self.folder,  self.problem)
        self.optimal_plan_cost_lower_bound = int(optimal_plan_cost_lower_bound)
        self.optimal_plan_cost_upper_bound = int(optimal_plan_cost_upper_bound)
        self.cost_bound = int(cost_bound)


def read_benchmarks_from_file(file_path, names):
    benchmarks = {}
    benchmarks_file = open(file_path, 'r')

    for line in benchmarks_file:
        if len(line) > 1 and line[0] is not '#':
            features = line.split(',')
            if (len(features) >= 8):
                key = features[0]
                if names is None or key in names:
                    if (not benchmarks.has_key(key)):
                        benchmarks[key] = []
                    benchmarks[key].append(Benchmark(features[1],
                                                     features[2],
                                                     features[3],
                                                     features[4],
                                                     features[5],
                                                     features[6],
                                                     features[7],
                                                     features[8]))
    benchmarks_file.close()

    return benchmarks


def test_container(image_path, benchmarks, results_path):
    results = []
    for benchmark_key, benchmark_instances in benchmarks.iteritems():
        benchmark_results_path = results_path + benchmark_key

        if not os.path.exists(benchmark_results_path):
            os.mkdir(benchmark_results_path)

        for benchmark in benchmark_instances:
            instance_path = benchmark_results_path + '/' + benchmark.problem[:-5]
            if not os.path.exists(instance_path):
                os.mkdir(instance_path)
            results.append(test_container_on_benchmark(image_path, benchmark, instance_path))

    return results

def test_container_multiProcessor(params):


    image_path = params[0]
    benchmarks = params[1]
    results_path = params[2]
    config = params[3]
    results = []

    for benchmark_key, benchmark_instances in benchmarks.iteritems():
        benchmark_results_path = results_path + benchmark_key

        if not os.path.exists(benchmark_results_path):
            os.mkdir(benchmark_results_path)

        for benchmark in benchmark_instances:
            instance_path = benchmark_results_path + '/' + benchmark.problem[:-5]
            if not os.path.exists(instance_path):
                os.mkdir(instance_path)
            results.append(test_container_on_benchmark(image_path, benchmark, instance_path, config))

    return results


def parse_val_output(output):

    match = re.search("Value: (\d+)", output)
    if "Plan valid" in output and match:
        return int(match.groups(1)[0])
    return None

def generate_info(domain_file, problem_file, plan_file, time):
    if time == None:
        return [VAL_PATH, domain_file, problem_file, plan_file]
    else:
        return [VAL_PATH, "-t", time, domain_file, problem_file, plan_file]

def clean_output_file(file):

    try:
        cleaned = open(file + ".cleaned", "w")
        founded = False

        with open(file) as f:
            for line in f:
                if line.__contains__('0.000:'):
                    founded = True
                if founded:
                    cleaned.write(line)

        cleaned.close()
    except IOError:
        return False

    return True

def verify_result(benchmark, run_dir, stdout, stderr, instance_path, config):

    options = [None]

    if (config.temporal_domains):
        options = ["0.0001", "0.001", "0.01", "0.1", None]

    valid_plan = False

    plans = list(glob.glob(os.path.join(run_dir, "sas_plan*")))

    if not plans:
        stderr.write("No plans generated.\n")
        return valid_plan
    for plan in plans:

        print "checking plan", plan
        copy(plan, os.path.join(instance_path, plan.split('/')[-1]))

        for option in options:
            info = generate_info(benchmark.domain_path, benchmark.problem_path, plan, option)

            if clean_output_file(plan):

                info[len(info)-1] = plan + ".cleaned"
                copy(info[len(info)-1], os.path.join(instance_path, info[len(info)-1].split('/')[-1]))
                print("checking plan" + info[len(info)-1] + " built from " + plan)

                try:
                    output = check_output(info, stderr=stderr).decode()
                    stdout.write(output)
                    plan_cost = parse_val_output(output)
                    if plan_cost is not None:
                        valid_plan = True
                        break
                    #if not (lb <= plan_cost <= ub):
                    #    stderr.write("Plan cost of %d is outside of expected bounds of [%d, %d].\n" % (plan_cost, lb, ub))
                    #    return False
                except CalledProcessError, err:
                    stderr.write(str(err))
                    print(err)
                    continue

    if valid_plan:
        print "verified", len(plans), "plans"
    else:
        print "plans could not be verified ", len(plans)
    return True


def test_container_on_benchmark(image_path, benchmark, instance_path, config):

    image_name = os.path.splitext(os.path.basename(image_path))[0]
    logs = LogFiles("%s-%s-%s" % (image_name, benchmark.folder, benchmark.problem[:-5]), instance_path)
    result = BenchmarkResult(benchmark, logs)
    print "Testing %s on domain %s(%s/%s) ..." % (image_name, benchmark.folder, benchmark.domain, benchmark.problem),
    sys.stdout.flush()

    # Singularity doesn't like its home directory below /tmp

    with TempDir(dir=SCRIPT_DIR) as run_dir, logs as (stdout, stderr):

        copy(benchmark.domain_path, os.path.join(run_dir, "domain.pddl"))
        copy(benchmark.problem_path, os.path.join(run_dir, "problem.pddl"))

        copy(benchmark.domain_path, os.path.join(instance_path, "domain.pddl"))
        copy(benchmark.problem_path, os.path.join(instance_path, "problem.pddl"))

        try:
            run_image(image_path, run_dir, [
                    "domain.pddl", "problem.pddl", "sas_plan", str(benchmark.cost_bound)
                ], stdout, stderr)
            print("running")
        except CalledProcessError, err:
            stderr.write(str(err))
        try:
            result.success = verify_result(benchmark, run_dir, stdout, stderr, instance_path, config)
        except CalledProcessError, err:
            stderr.write(str(err))
    print "ok" if result.success else "failed"
    return result
