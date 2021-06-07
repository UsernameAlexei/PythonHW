# TIME CHECK
from timeit import timeit

from Profiling_task import football_1, football_2, list_transformation_1, list_transformation_2, \
    list_transformation_3, bubble_sort, selection_sort, unpacking_1, unpacking_2

# parameters
City = ['Athens', 'Paris', 'St Louis', 'London', 'Stockholm', 'Antwerp', 'Amsterdam',
        'Los Angeles', 'Berlin', 'Helsinki', 'Melbourne / Stockholm', 'Rome', 'Tokyo',
        'Mexico', 'Munich', 'Montreal', 'Moscow', 'Seoul', 'Barcelona', 'Atlanta',
        'Sydney', 'Beijing']

arr = [5, 2, 1, 8, 4, 3, 6, 7, 9]

unpacking_list = [['E', 'L', 'O', 'N'], ['M', 'U', 'S', 'K']]

# CHECK
pandas_time = timeit(stmt='football_1(x)', setup="x='home_team'", number=10, globals=globals())
csv_time = timeit(stmt='football_2(x)', setup="x='home_team'", number=10, globals=globals())

list_transformation_time_1 = timeit(stmt='list_transformation_1(City)', number=1000, globals=globals())
list_transformation_time_2 = timeit(stmt='list_transformation_2(City)', number=1000, globals=globals())
list_transformation_time_3 = timeit(stmt='list_transformation_3(City)', number=1000, globals=globals())

bubble_sort_time = timeit(stmt='bubble_sort(arr)', number=1000, globals=globals())
selection_sort_time = timeit(stmt='selection_sort(arr)', number=1000, globals=globals())

unpacking_time_1 = timeit(stmt='unpacking_1(unpacking_list)', number=1000, globals=globals())
unpacking_time_2 = timeit(stmt='unpacking_2(unpacking_list)', number=1000, globals=globals())

print(f'pandas time: {pandas_time}\ncsv time: {csv_time}')
print(f'list_transformation_time_1: {list_transformation_time_1}')
print(f'list_transformation_time_2: {list_transformation_time_2}')
print(f'list_transformation_time_3: {list_transformation_time_3}')
print(f'bubble_sort_time: {bubble_sort_time}\nselection_sort_time: {selection_sort_time}')
print(f'unpacking_time_1: {unpacking_time_1}\nunpacking_time_2: {unpacking_time_2}')