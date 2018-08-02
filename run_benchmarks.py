#!/usr/bin/env python

import cPickle as pickle
import multiprocessing
import os
# from subprocess import check_call, CalledProcessError
import sys
import argparse
from collections import defaultdict
from multiprocessing import Pool

# from repo import detect_repo_type, get_up_to_date_repo, get_tag_revision, update
from benchmarks import test_container_multiProcessor, read_benchmarks_from_file
from config import PLANNER_DIR, IMAGES_DIR, RESULT_CACHE, RESULT_OUTPUT, IPC2018_BENCHMARKS, TIPC2018_BENCHMARKS, IPC2018_PLANNERS, TIPC2018_PLANNERS, DEFAULT_NUMBER_PROCESSOR
from planners import read_planners_from_file
from results import Result
from results_info import getResultsForPlanner
from singularity import try_build_image, try_extract_labels


def file_exists(path, force_overwrite):
    if os.path.exists(path):
        #prompt = "%s already exists. Do you want to overwrite it? [y/N] " % path
        #if force_overwrite or raw_input(prompt).strip().lower() == 'y':
        if force_overwrite:
            os.remove(path)
        else:
            return True
    return False

def create_and_test_image(planner_name, planners, benchmarks=None, stored_result=None, cpu_number=DEFAULT_NUMBER_PROCESSOR, force_overwrite=False):
    result = Result()
    test_params = []

    #pool = Pool(cpu_number)
    pool = Pool(1)
    image_path = os.path.join(IMAGES_DIR, "%s.img" % (planner_name))

    if file_exists(image_path, force_overwrite):
        print("Build skipped because file exists")
    else:
        # Build the image.
        print("Building %s" % image_path)
        planner_path = os.path.join(PLANNER_DIR, "%s" % (planners[planner_name].getFolder()))
        result.build_successful, result.build_logs = try_build_image(planner_path, image_path, planner_name)

        if not result.build_successful:
            print("Building %s failed" % image_path)
            return result
        print("Successfully built %s" % image_path)

    results_path = os.path.join(RESULT_OUTPUT, "%s/" % (planner_name))

    if not os.path.exists(results_path):
        os.mkdir(results_path)

    for key, values in benchmarks.iteritems():

        for value in values:
            #print value
            benchmark = {key: [value]}
            #print benchmark
            test_params.append([""+image_path, benchmark, ""+results_path])


    #TODO: fix KeyboardInterrupt bug - https://jreese.sh/blog/python-multiprocessing-keyboardinterrupt https://stackoverflow.com/questions/21104997/keyboard-interrupt-with-pythons-multiprocessing/21106459#21106459
    # Test the image, each domain receives a different processor.
    pool.map(test_container_multiProcessor, test_params)

    #result.benchmark_results = test_container(image_path, benchmarks, results_path)
    result.labels = try_extract_labels(image_path)

    return result

def create_and_test_images(planner_names, planners, benchmarks = None, results=defaultdict(dict), cpu_number=DEFAULT_NUMBER_PROCESSOR, force_overwrite=False):
    oldmask = os.umask(022)
    for planner in planner_names:
        stored_result = None #results[planner].get(track)
        result = create_and_test_image(planner, planners, benchmarks, stored_result, cpu_number, force_overwrite)
        results[planner] = result
    os.umask(oldmask)
    return results

def load_stored_results():
    with open(RESULT_CACHE, "rb") as f:
        return pickle.load(f)

def save_stored_results(results):
    with open(RESULT_CACHE, "wb") as f:
        pickle.dump(results, f)

def cached_create_and_test_images(planners_names, planners, benchmarks, cpu_number, force_overwrite=False):
    stored_results = defaultdict(dict)
    results = create_and_test_images(planners_names, planners, benchmarks, stored_results, cpu_number, force_overwrite)
    save_stored_results(results)
    return results

if __name__ == "__main__":

    ipc = False
    tipc = False

    planners_names = []
    benchmarks = {}
    cpu_number = DEFAULT_NUMBER_PROCESSOR

    parser = argparse.ArgumentParser(description='Planning tool to run planners and domains using singularity containers.')

    parser.add_argument('-b', metavar='benchmarks domains',
                        help='a path to the file with the information about the different benchmarks.')
    parser.add_argument('-p', metavar='planners',
                        help='a path to the file with the information about the different planners which can be executed.')
    parser.add_argument('-t', metavar='temporal', action='store_const', const=True, default=False,
                        help='a boolean parameter which activate temporal validation')
    parser.add_argument('-ipc2018', metavar='temporal', action='store_const', const=True, default=False,
                        help='a boolean parameter which run ipc 2018')
    parser.add_argument('-tipc2018', metavar='temporal', action='store_const', const=True, default=False,
                        help='a boolean parameter which run temporal ipc 2018')
    parser.add_argument('-proc', metavar='cpu numbers',
                        help='a number parameter which defines the maximum number of cpus (threads). Default value is value is ')
    parser.add_argument('-pn', metavar='planner names', nargs='+',
                        help='a list parameter which defines the names of the planner which are going to be executed')
    parser.add_argument('-bn', metavar='planner names', nargs='+',
                        help='a list parameter which defines the names of the benchmarks which are going to be used')
    parser.add_argument("--v", metavar='verbosity', action='store_const', const=True, default=False,
                        help="increase output verbosity")

    args = parser.parse_args()

    verbosity = True if args.v else False
    temporal = True if args.t else False

    if args.ipc2018:
        benchmarks = read_benchmarks_from_file(IPC2018_BENCHMARKS, args.bn)
        planners = read_planners_from_file(IPC2018_PLANNERS, args.pn)
    elif args.tipc2018:
        benchmarks = read_benchmarks_from_file(TIPC2018_BENCHMARKS, args.bn)
        planners = read_planners_from_file(TIPC2018_PLANNERS, args.pn)
        temporal = True
    elif args.b is not None and args.p is not None:
        if os.path.isfile(args.b):
            benchmarks = read_benchmarks_from_file(args.b, args.bn)
            if os.path.isfile(args.p):
                planners = read_planners_from_file(args.p, args.pn)
            else:
                print('Error: planner file %s does not exit', args.p)
        else:
            print('Error: benchmarks file %s does not exit', args.b)
    else:
        parser.print_usage()

    if args.proc is not None:
        if args.proc > multiprocessing.cpu_count():
            cpu_number = multiprocessing.cpu_count()
        else:
            cpu_number = args.proc

    planners_names = args.pn if args.pn is not None else planners.keys()

    if not os.path.exists(RESULT_OUTPUT):
        os.mkdir(RESULT_OUTPUT)

    if not os.path.exists(IMAGES_DIR):
        os.mkdir(IMAGES_DIR)

    cached_create_and_test_images(planners_names, planners, benchmarks, cpu_number, False)

    for planner in planners_names:
        getResultsForPlanner(planner)