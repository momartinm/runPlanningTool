#!/usr/bin/env python

import glob
import os
import re
import sys
from shutil import copy
from subprocess import check_output, CalledProcessError

from paths import LogFiles, TempDir, PLANNER_BENCHMARKS_DIR, SCRIPT_DIR, RESULT_OUTPUT, VAL_PATH, TEMPORAL_DOMAINS
from singularity import run_image

from results import BenchmarkResult

class Benchmark(object):
    def __init__(self, folder, domain, problem, domain_path=None, problem_path=None,
                 optimal_plan_cost_lower_bound=None, optimal_plan_cost_upper_bound=None, cost_bound=2147483647):
        self.folder = folder
        self.domain = domain
        self.problem = problem
        self.domain_path = domain_path or os.path.join(PLANNER_BENCHMARKS_DIR, folder, domain)
        self.problem_path = problem_path or os.path.join(PLANNER_BENCHMARKS_DIR, folder, problem)
        self.optimal_plan_cost_lower_bound = optimal_plan_cost_lower_bound
        self.optimal_plan_cost_upper_bound = optimal_plan_cost_upper_bound
        self.cost_bound = cost_bound


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

def verify_result(benchmark, run_dir, stdout, stderr, instance_path):

    options = [None]

    if (TEMPORAL_DOMAINS):
        options = ["0.0001", "0.001", "0.01", "0.1", None]

    valid_plan = False

    plans = list(glob.glob(os.path.join(run_dir, "sas_plan*")))

    if not plans:
        stderr.write("No plans generated.\n")
        return False
    for plan in plans:
        print "checking plan", plan
        copy(plan, os.path.join(instance_path, plan.split('/')[-1]))

        for option in options:
            info = generate_info(benchmark.domain_path, benchmark.problem_path, plan, option)
            print "checking plan", plan
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
    print "verified", len(plans), "plans"
    return True


def test_container_on_benchmark(image_path, benchmark, instance_path):

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
            result.success = verify_result(benchmark, run_dir, stdout, stderr, instance_path)
        except CalledProcessError, err:
            stderr.write(str(err))
    print "ok" if result.success else "failed"
    return result
