# TASK 1-4

import csv
import pandas as pd


# 1 read and write way 1
def read_write_1(x=None, data=None):
    if x is None:
        return None
    else:
        df = pd.read_csv(data)
        df_dict = df.to_dict()
        return df_dict[x]


# 1 read and write way 2
def read_write_2(x=None, data=None):
    d = {}
    if x is None:
        return None
    else:
        reader = csv.DictReader(open(data))
        for i, s in enumerate(reader):
            d[i] = s[x]
    return d


# 2 list transformation way 1
def list_transformation_1(cities):
    cities_1 = []
    for i in cities:
        cities_1.append(i.upper())
    return cities_1


# 2 list transformation way 2
def list_transformation_2(cities):
    cities_2 = [x.upper() for x in cities]
    return cities_2


# 2 list transformation way 3
def list_transformation_3(cities):
    cities_3 = list(map(lambda x: x.upper(), cities))
    return cities_3


# 3 sorting the list way 1
def pd_sort_values(arr):
    df = {}
    df['number'] = arr
    df = pd.DataFrame(df)
    return df.sort_values(by='number')


# 3 sorting the list way 2
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


# 3 sorting the list way 2
def method_sorted(arr):
    return sorted(arr)


# 4 unpacking a nested list way 1
# calculates the depth of the inner list
def count_list(l):
    count = 0
    for e in l:
        if isinstance(e, list):
            count = count + 1 + count_list(e)
    return count


def unpacking_1(unpacking_list):
    s = []
    for i in range(count_list(unpacking_list)):
        if i >= 1:
            unpacking_list = s
            s = []
        for y in range(len(unpacking_list)):
            try:
                for x in unpacking_list[y]:
                    s.append(x)
            except TypeError:
                s.append(unpacking_list[y])
    return unpacking_list


# 4 unpacking a nested list way 2
def unpacking_2(unpacking_list):
    return [next_value for next_list in unpacking_list for next_value in next_list]
