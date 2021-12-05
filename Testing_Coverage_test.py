import time
import unittest
from Testing_Coverage_task import cached, CACHE, my_range

# Test_Task 1
class Test_task1_my_range(unittest.TestCase):

    def test_generation_all_positive(self):
        result = list(my_range(5, 11, 2))
        self.assertEqual(result, [5, 7, 9])

    def test_generation_all_negative(self):
        result = list(my_range(-5, -11, -2))
        self.assertEqual(result, [-5, -7, -9])

    def test_generation_start_stop(self):
        result = list(my_range(5, 11))
        self.assertEqual(result, [5, 6, 7, 8, 9, 10])

    def test_generation_start_stop_negative(self):
        result = list(my_range(-5, -11))
        self.assertEqual(result, [])

    def test_generation_start(self):
        result = list(my_range(5))
        self.assertEqual(result, [0, 1, 2, 3, 4])

    def test_generation_start_negative(self):
        result = list(my_range(-5))
        self.assertEqual(result, [])

    def test_empty(self):
        result = list(my_range())
        self.assertEqual(result, [])

    #negative test
    def test_type(self):
        result = list(my_range('str'))
        self.assertEqual(result, 'Type error, enter numeric values')

    def test_format(self):
        result = list(my_range(1, 2, 3, 4))
        self.assertEqual(result, 'Takes from 0 to 3 positional arguments')


# Test_Task2
@cached(use_cache=True)
def mul(x):
    time.sleep(2)
    return x * 2

class Test_task2_cached(unittest.TestCase):

    def test_caching(self):
        mul(2)
        result = CACHE
        self.assertEqual(result, {(2,): 4})

    def test_from_cache(self):
        CACHE.clear()
        start_time = time.time()
        mul(2)
        call_mul_1 = time.time() - start_time

        start_time = time.time()
        mul(2)
        call_mul_2 = time.time() - start_time
        assert (call_mul_1 > call_mul_2)

    def test_caching_str(self):
        CACHE.clear()
        mul('str')
        result = CACHE
        self.assertEqual(result, {('str',): 'strstr'})

    # negative test
    def test_caching_empty(self):
        result = mul()
        self.assertEqual(result, 'Missing 1 required positional argument')


if __name__ == '__main__':
    unittest.main()
