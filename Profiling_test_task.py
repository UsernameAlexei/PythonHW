# pytest
import csv

import pandas as pd

from Profiling_task import read_write_1, read_write_2, list_transformation_1, list_transformation_2, \
    list_transformation_3, method_sorted, selection_sort, unpacking_1, unpacking_2, pd_sort_values, count_list

# create a file for testing 1 read and write
s_line_1 = r'date', 'home_team', 'away_team', 'home_score', 'away_score', 'tournament', 'city', 'country', 'neutral'
s_line_2 = r'2021-01-12', 'United Arab Emirates', 'Iraq', '0', '0', 'Friendly', 'Dubai', 'United Arab Emirates', 'FALSE'
s_line_3 = r'2021-01-18', 'Kuwait', 'Palestine', '0', '1', 'Friendly', 'Kuwait City', 'Kuwait', 'FALSE '

with open('some.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(s_line_1)

with open('some.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(s_line_2)
    wr.writerow(s_line_3)

# parameters for testing 2 list transformation
cities = ['Athens', 'Paris', 'St Louis', 'London', 'Stockholm']
result_list_transform = ['ATHENS', 'PARIS', 'ST LOUIS', 'LONDON', 'STOCKHOLM']

# parameters for testing 3 sort
arr = [5, 2, 1, 8, 4, 3, 6, 7, 9]
result_sort = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pd_arr_result = pd.DataFrame({'number': [1, 2, 3, 4, 5, 6, 7, 8, 9]},
                             index=[2, 1, 5, 4, 0, 6, 7, 3, 8])
# parameters for testing 4 unpacking
unpacking_list = [[1, 0, 1], ['E', 'L', 'O', 'N']]
result_unpacking = [1, 0, 1, 'E', 'L', 'O', 'N']


# Test 1 read and write way 1
def test_read_write_1():
    result = {0: 'United Arab Emirates', 1: 'Kuwait'}
    assert result == read_write_1('home_team', 'some.csv')


# Test 1 read and write way 2
def test_read_write_2():
    result = {0: 'United Arab Emirates', 1: 'Kuwait'}
    assert result == read_write_2('home_team', 'some.csv')


# Test 2 list transformation way 1
def test_list_transformation_1():
    assert list_transformation_1(cities) == result_list_transform


# Test 2 list transformation way 2
def test_list_transformation_2():
    assert list_transformation_2(cities) == result_list_transform


# Test 2 list transformation way 3
def test_list_transformation_3():
    assert list_transformation_3(cities) == result_list_transform


# Test 3 list transformation way 1
def test_pd_sort_values():
    assert pd_sort_values(arr).equals(pd_arr_result)


# Test 3 list transformation way 2
def test_selection_sort():
    assert selection_sort(arr) == result_sort


# Test 3 list transformation way 3
def test_method_sort():
    assert method_sorted(arr) == result_sort


# Test 4 list transformation way 1
def test_unpacking_1():
    assert unpacking_1(unpacking_list) == result_unpacking


# Test 4 list transformation way 2
def test_unpacking_2():
    assert unpacking_2(unpacking_list) == result_unpacking
