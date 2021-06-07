# TASK 1-4
# 1 read and write way 1
import csv
import pandas as pd


def football_1(x=None):
    if x is None:
        return None
    else:
        df = pd.read_csv('football_results.csv')
        df_dict = df.to_dict()
        return df_dict[x]


# 1 read and write way 2
def football_2(x=None):
    d = {}
    if x is None:
        return None
    else:
        reader = csv.DictReader(open('football_results.csv'))
        for i, s in enumerate(reader):
            d[i] = s[x]
    return d


# 2 list transformation way 1
def list_transformation_1(City):
    City_1 = []
    for i in City:
        City_1.append(i.upper())
    return City_1


# 2 list transformation way 2
def list_transformation_2(City):
    City_2 = [x.upper() for x in City]
    return City_2


# 2 list transformation way 3
def list_transformation_3(City):
    City_3 = list(map(lambda x: x.upper(), City))
    return City_3


# 3 sorting the list way 1
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr


# 3 sorting the list way 2
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


# 4 unpacking a nested list way 1
def unpacking_1(un_list):
    up_1 = " ".join(" ".join(L) for L in un_list)
    return up_1


# 4 unpacking a nested list way 2
def unpacking_2(un_list):
    up_2 = []
    for i in un_list:
        up_2 += i
    return " ".join(up_2)
