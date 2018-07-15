#!/usr/bin/env python

from collections import defaultdict
from benchmarks_files import ALL_BENCHMARKS
from planners import ALL_PLANNERS

import cPickle as pickle
import os
from subprocess import check_call, CalledProcessError
import sys

from paths import PLANNER_DIR, REPO_DIR, IMAGES_DIR, RESULT_CACHE, RESULT_OUTPUT
from repo import detect_repo_type, get_up_to_date_repo, get_tag_revision, update
from benchmarks import test_container
from singularity import try_build_image, try_extract_labels
from results import Result

def file_exists(path, force_overwrite):
    if os.path.exists(path):
        #prompt = "%s already exists. Do you want to overwrite it? [y/N] " % path
        #if force_overwrite or raw_input(prompt).strip().lower() == 'y':
        if force_overwrite:
            os.remove(path)
        else:
            return True
    return False

def create_and_test_image(planner_name, benchmarks=None, stored_result=None, force_overwrite=False):
    result = Result()

    image_path = os.path.join(IMAGES_DIR, "%s.img" % (planner_name))

    if file_exists(image_path, force_overwrite):
        print("Build skipped because file exists")
    else:
        # Build the image.
        print("Building %s" % image_path)
        planner_path = os.path.join(PLANNER_DIR, "%s" % (ALL_PLANNERS[planner_name].getFolder()))
        result.build_successful, result.build_logs = try_build_image(planner_path, image_path, planner_name)
        if not result.build_successful:
            print("Building %s failed" % image_path)
            return result
        print("Successfully built %s" % image_path)

    results_path = os.path.join(RESULT_OUTPUT, "%s/" % (planner_name))

    if not os.path.exists(results_path):
        os.mkdir(results_path)

    # Test the image.
    result.benchmark_results = test_container(image_path, benchmarks, results_path)
    result.labels = try_extract_labels(image_path)

    return result

def create_and_test_images(planner_names, benchmarks = None, results=defaultdict(dict), force_overwrite=False):
    oldmask = os.umask(022)
    for planner in planner_names:
        stored_result = None #results[planner].get(track)
        result = create_and_test_image(planner, benchmarks, stored_result, force_overwrite)
        results[planner] = result
    os.umask(oldmask)
    return results

def load_stored_results():
    with open(RESULT_CACHE, "rb") as f:
        return pickle.load(f)

def save_stored_results(results):
    with open(RESULT_CACHE, "wb") as f:
        pickle.dump(results, f)

def cached_create_and_test_images(planners_names, benchmarks, force_overwrite=False):
    stored_results = defaultdict(dict)
    results = create_and_test_images(planners_names, benchmarks, stored_results, force_overwrite)
    save_stored_results(results)
    return results

if __name__ == "__main__":

    planners_names = []
    benchmarks = {}

    for arg in sys.argv[1:]:
        if arg in ALL_PLANNERS.keys():
            planners_names.append(arg)
        elif arg in ALL_BENCHMARKS.keys():
            benchmarks[arg] = ALL_BENCHMARKS.get(arg)
        else:
            print "Arguments must be valid track or team names. Change the variables ALL_TRACKS and ALL_TEAMS in this script to build other images."
            sys.exit(1)

    planners_names = planners_names or ALL_PLANNERS.keys()
    benchmarks = benchmarks or ALL_BENCHMARKS

    if not os.path.exists(RESULT_OUTPUT):
        os.mkdir(RESULT_OUTPUT)

    if not os.path.exists(IMAGES_DIR):
        os.mkdir(IMAGES_DIR)

    cached_create_and_test_images(planners_names, benchmarks, False)