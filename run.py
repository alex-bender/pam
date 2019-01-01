#!/usr/bin/env python3
"""Launch tests, check function efficiency
NOTES:
    https://hakibenita.com/timing-tests-in-python-for-fun-and-profit
"""
import time
import unittest
from unittest import TextTestRunner
from unittest.runner import TextTestResult


SLOW_TEST_THRESHOLD = 0

class TimeLoggingTestRunner(unittest.TextTestRunner):

    def __init__(self, slow_test_threshold=0.3, *args, **kwargs):
        self.slow_test_threshold = slow_test_threshold
        return super().__init__(resultclass=TimeLoggingTestResult, *args, **kwargs)

    def run(self, test):
        result = super().run(test)

        self.stream.writeln("\nSlow Tests (>{:.03}s):".format(self.slow_test_threshold))
        for name, elapsed in result.getTestTimings():
            if elapsed > self.slow_test_threshold:
                self.stream.writeln("({:.03}s) {}".format(elapsed, name))

        return result


class TimeLoggingTestResult(TextTestResult):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_timings = []

    def startTest(self, test):
        self._started_at = time.time()
        super().startTest(test)

    def addSuccess(self, test):
        elapsed = time.time() - self._started_at
        name = self.getDescription(test)
        self.test_timings.append((name, elapsed))
        super().addSuccess(test)

    def getTestTimings(self):
        return self.test_timings

if __name__ == '__main__':
    # TODO: add argument parser, get module name
    test_runner = TimeLoggingTestRunner()
    from subprocess import call
    call(["bat", "task_test.py"])
    unittest.main(module='task_test', testRunner=test_runner)
