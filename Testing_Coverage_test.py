import unittest
from Testing_Coverage_task import  cached, my_range

#Test_Task 1
class Test_task1_my_range(unittest.TestCase):

    def test_generation_all_positive(self):
        result = list(my_range(5, 11, 2))
        self.assertEqual(result, [5,7,9])

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
        result = list(my_range(1,2,3,4))
        self.assertEqual(result, 'Takes from 0 to 3 positional arguments')


#Test_Task2
@cached(use_cache=True)
def mul(x):
    return x*2

class Test_task2_cached(unittest.TestCase):

    def test_caching(self):
        result = mul(2)
        self.assertEqual(result, f'caching 4')

    def test_from_cache(self):
        result = mul(2)
        self.assertEqual(result, f'from cache 4')

    def test_caching_str(self):
        result = mul('str')
        self.assertEqual(result, f'caching strstr')

    def test_from_cache_str(self):
        result = mul('str')
        self.assertEqual(result, f'from cache strstr')

    # negative test
    def test_caching_empty(self):
        result = mul()
        self.assertEqual(result, 'Missing 1 required positional argument')


if __name__ == '__main__':
    unittest.main()