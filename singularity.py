import os
import resource
from shutil import copy, copytree, rmtree, Error
from subprocess import check_call, check_output, CalledProcessError
import sys
from vagrant import Vagrant
import json

from config import makedirs, LogFiles, SINGULARITY_VM, SINGULARITY_VM_INPUT_DIR, \
  SINGULARITY_VM_OUTPUT_DIR, SINGULARITY_VM_IMAGE, SINGULARITY_VM_STDOUT, \
  SINGULARITY_VM_STDERR, CONFIG_MEMORY_LIMIT, CONFIG_TIME_LIMIT

MEMORY_LIMIT = CONFIG_MEMORY_LIMIT * 1024 * 1024 * 1024 # 8 GB

def prepare_call():
    set_limit(resource.RLIMIT_CPU, CONFIG_TIME_LIMIT, CONFIG_TIME_LIMIT + 5)
    set_limit(resource.RLIMIT_AS, MEMORY_LIMIT)
    set_limit(resource.RLIMIT_CORE, 0)

def set_limit(kind, soft_limit, hard_limit=None):
    if hard_limit is None:
        hard_limit = soft_limit
    try:
        resource.setrlimit(kind, (soft_limit, hard_limit))
    except (OSError, ValueError), err:
        sys.stderr.write(
            'Resource limit for %s could not be set to %s (%s)\n' %
            (kind, (soft_limit, hard_limit), err))

def run_image(image_path, home_dir, args, stdout, stderr):
    check_call([
        "singularity", "run", "-C", "-H", home_dir, image_path] + args,
        stdout=stdout, stderr=stderr, preexec_fn=prepare_call)

class SingularityVM(object):
    def __init__(self, path_to_build):
        self.path_to_build = path_to_build

    def __enter__(self):
        # We want to start with a clean environment every time.
        if os.path.exists(SINGULARITY_VM_INPUT_DIR):
            rmtree(SINGULARITY_VM_INPUT_DIR)
        if os.path.exists(SINGULARITY_VM_OUTPUT_DIR):
            rmtree(SINGULARITY_VM_OUTPUT_DIR)
        makedirs(SINGULARITY_VM_OUTPUT_DIR)
        copytree(self.path_to_build, SINGULARITY_VM_INPUT_DIR, symlinks=True)
        self.vm = Vagrant(root=SINGULARITY_VM, quiet_stdout=False, quiet_stderr=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.vm.destroy()
        rmtree(SINGULARITY_VM_INPUT_DIR)
        rmtree(SINGULARITY_VM_OUTPUT_DIR)

    def run(self):
        try:
            self.vm.up()
            return SINGULARITY_VM_IMAGE
        except CalledProcessError:
            return None

    def store_logs(self, log_path, err_path):
        copy(SINGULARITY_VM_STDOUT, log_path)
        copy(SINGULARITY_VM_STDERR, err_path)


def try_extract_labels(image_path):
    try:
        json_labels = check_output(["singularity", "inspect", "-l", image_path]).decode()
        return json.loads(json_labels)
    except CalledProcessError:
        return {}


def try_build_image(repo_dir, image_path, team_name):
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    logs = LogFiles(team_name, image_name)
    try:
        with SingularityVM(repo_dir) as vm:
            generated_image = vm.run()
            vm.store_logs(logs.log_path, logs.err_path)
            if generated_image:
                makedirs(os.path.dirname(image_path))
                copy(generated_image, image_path)
                return True, logs
            return False, logs
    except Error, errors:
        print "Failed to copy input files"
        with open(logs.err_path, "w") as f:
            f.write("Creating the Singularity image failed with the following errors:\n")
            for err in errors.args[0]:
                f.write("Exception when copying '%s' to '%s': %s\n" % err)
        return False, logs
