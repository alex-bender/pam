import time
import unittest
from task import function

SLOW_TEST_THRESHOLD = 0.00


class TaskTest(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > SLOW_TEST_THRESHOLD:
            print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

    def test_one(self):
        self.assertEqual(1, function(1))


if __name__ == '__main__':
    unittest.main()
