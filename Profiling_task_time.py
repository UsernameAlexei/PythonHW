# TIME CHECK
from timeit import timeit

import pandas as pd

from Profiling_task import read_write_1, read_write_2, list_transformation_1, list_transformation_2, \
    list_transformation_3, pd_sort_values, selection_sort, unpacking_1, unpacking_2

# parameters
cities = ['Athens', 'Paris', 'St Louis', 'London', 'Stockholm']

arr = [5, 2, 1, 8, 4, 3, 6, 7, 9]

unpacking_list = [[1, 0, 1], ['E', 'L', 'O', 'N']]

# CHECK
# time 1 read_write
setup_read_write_1 = """
x='City'
data='olimpic_medals100k.csv'
"""
pandas_time_100k = timeit(stmt='read_write_1(x, data)', setup=setup_read_write_1, number=1, globals=globals())
csv_time_100k = timeit(stmt='read_write_2(x, data)', setup=setup_read_write_1, number=1, globals=globals())

setup_read_write_2 = """
x='City'
data='olimpic_medals1k.csv'
"""
pandas_time_1k = timeit(stmt='read_write_1(x, data)', setup=setup_read_write_2, number=1, globals=globals())
csv_time_1k = timeit(stmt='read_write_2(x, data)', setup=setup_read_write_2, number=1, globals=globals())

result_testing_read_write = {'Module': ['Pandas', 'CSV'],
                             '100k rows': [pandas_time_100k, csv_time_100k],
                             '1k rows': [pandas_time_1k, csv_time_1k]}

result_testing_read_write = pd.DataFrame(result_testing_read_write)
print(result_testing_read_write)

# time 2 list_transformation
list_transformation_time_1 = timeit(stmt='list_transformation_1(cities)', number=1000, globals=globals())
list_transformation_time_2 = timeit(stmt='list_transformation_2(cities)', number=1000, globals=globals())
list_transformation_time_3 = timeit(stmt='list_transformation_3(cities)', number=1000, globals=globals())

list_transformation_time_1_plus = timeit(stmt='list_transformation_1(cities*1000)', number=1000, globals=globals())
list_transformation_time_2_plus = timeit(stmt='list_transformation_2(cities*1000)', number=1000, globals=globals())
list_transformation_time_3_plus = timeit(stmt='list_transformation_3(cities*1000)', number=1000, globals=globals())

result_testing_list_transform = {
    'Name': ['list_transformation_1', 'list_transformation_2', 'list_transformation_3'],
    '5 values': [list_transformation_time_1, list_transformation_time_2, list_transformation_time_3],
    '5k values': [list_transformation_time_1_plus, list_transformation_time_2_plus, list_transformation_time_3_plus]}

result_testing_list_transform = pd.DataFrame(result_testing_list_transform)

print(result_testing_list_transform)

# time 3 sort
pd_sort_values = timeit(stmt="pd_sort_values(arr)", number=10000, globals=globals())
selection_sort_time = timeit(stmt='selection_sort(arr)', number=10000, globals=globals())
method_sorted_time = timeit(stmt='sorted(arr)', number=10000, globals=globals())

result_testing_sort = {
    'Name': ['pandas_sort_values', 'selection_sort', 'method_sorted', ],
    '9 values': [pd_sort_values, selection_sort_time, method_sorted_time, ]}

result_testing_sort = pd.DataFrame(result_testing_sort)
print(result_testing_sort)

# time 4 unpacking
unpacking_time_1 = timeit(stmt='unpacking_1(unpacking_list)', number=1000, globals=globals())
unpacking_time_2 = timeit(stmt='unpacking_2(unpacking_list)', number=1000, globals=globals())

result_testing_unpacking = {
    'Name': ['unpacking1', 'unpacking2'],
    '9 values': [unpacking_time_1, unpacking_time_2]}

result_testing_unpacking = pd.DataFrame(result_testing_unpacking)
print(result_testing_unpacking)
