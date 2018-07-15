class BenchmarkResult(object):
    def __init__(self, benchmark, logs):
        self.benchmark = benchmark
        self.logs = logs
        self.success = False

class Result(object):
    SUCCESS = 0
    TAG_NOT_FOUND = 1
    BUILD_FAILED = 2
    BENCHMARKS_FAILED = 3

    def __init__(self):
        self.revision = None
        self.build_successful = None
        self.build_logs = None
        self.benchmark_results = []
        self.labels = {}

    def get_failure_level(self):
        if self.revision is None:
            return Result.TAG_NOT_FOUND
        assert self.build_successful is not None
        if not self.build_successful:
            return Result.BUILD_FAILED
        if any(not r.success for r in self.benchmark_results):
            return Result.BENCHMARKS_FAILED
        return Result.SUCCESS

    @staticmethod
    def unpickle(data):
        out = pickle.loads(data)
        if not hasattr(out, 'labels'):
            out.labels = {}
        return out
