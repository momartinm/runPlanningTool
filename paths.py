import os
import shutil
import tempfile
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_DIR = os.path.join(SCRIPT_DIR, "repositories")
LOGS_DIR = os.path.join(SCRIPT_DIR, "logs")
IPC_LOGS_DIR = os.path.join(SCRIPT_DIR, "ipc_logs")
IMAGES_DIR = os.path.join(SCRIPT_DIR, "images")
PLANNER_BENCHMARKS_DIR = os.path.join(SCRIPT_DIR, "benchmarks")
PLANNER_DIR = os.path.join(SCRIPT_DIR, "planners")
RESULT_OUTPUT = os.path.join(SCRIPT_DIR, "results")
RESULT_CACHE = os.path.join(SCRIPT_DIR, ".last_results.pickle")

VAL_PATH = os.path.join(SCRIPT_DIR, "validate")
TEMPORAL_DOMAINS = True

SINGULARITY_VM = os.path.join(SCRIPT_DIR, "singularityvm")
SINGULARITY_VM_INPUT_DIR = os.path.join(SINGULARITY_VM, "input")
SINGULARITY_VM_OUTPUT_DIR = os.path.join(SINGULARITY_VM, "output")
SINGULARITY_VM_IMAGE = os.path.join(SINGULARITY_VM_OUTPUT_DIR, "container.img")
SINGULARITY_VM_STDOUT = os.path.join(SINGULARITY_VM_OUTPUT_DIR, "build.log")
SINGULARITY_VM_STDERR = os.path.join(SINGULARITY_VM_OUTPUT_DIR, "build.err")


def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        # Directory probably already exists.
        pass

def rmtree(path):
    try:
        shutil.rmtree(path)
    except OSError:
        # Directory probably doesn't exist.
        pass


class LogFiles(object):
    def __init__(self, name, path = None):

        if (path is None):
            self.log_path = os.path.join(IPC_LOGS_DIR + "/" + name + ".log")
            self.err_path = os.path.join(IPC_LOGS_DIR + "/" + name + ".err")
        else:
            self.log_path = os.path.join(path + "/" + name + ".log")
            self.err_path = os.path.join(path + "/" + name + ".err")
        makedirs(os.path.dirname(self.log_path))
        makedirs(os.path.dirname(self.err_path))
        self.file_handles = None

    def __enter__(self):
        self.file_handles = open(self.log_path, "w").__enter__(), open(self.err_path, "w").__enter__()
        return self.file_handles

    def __exit__(self, exc_type, exc_val, exc_tb):
        for x in self.file_handles:
            x.__exit__(exc_type, exc_val, exc_tb)
        self.file_handles = None


class TempDir(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        self.path = tempfile.mkdtemp(*self.args, **self.kwargs)
        subprocess.call(['chmod', '-R', '+w', self.path])
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.path)
        pass
