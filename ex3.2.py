import json
import timeit
import matplotlib.pyplot as plt
import random


def binary_search_func(array, configured_midpoint, value_to_search):
    first = 0
    mid = configured_midpoint
    last = len(array) - 1

    while (first <= last):
        if (value_to_search < array[mid]):
            last = mid - 1
        elif (value_to_search > array[mid]):
            first = mid + 1
        else:
            return mid
        mid = (first + last) // 2
    return -1


with open("ex2data.json", "r") as data:
    array = json.load(data)

with open("ex2tasks.json", "r") as tasks:
    array_of_tasks = json.load(tasks)


midpoint_times = []
midpoint_with_best_times = []

for task in array_of_tasks:
    rand = random.randint(0, len(array))
    time = timeit.timeit(lambda: binary_search_func(
        array, rand, task), number=1)
    midpoint_times.append(time)

    best_mid = array[0] + (task - array[0]) * \
        (array[-1] - array[0]) // (array[-1] - array[0])
    time_best = timeit.timeit(lambda: binary_search_func(
        array, best_mid, task), number=1)
    midpoint_with_best_times.append(time_best)


plt.scatter(x=array_of_tasks, y=midpoint_times, c="y", label="midpoints")
plt.scatter(x=array_of_tasks, y=midpoint_with_best_times,
            c="g", label="midpoints_best")
plt.xlabel("Tasks Values")
plt.ylabel("Run Time (s)")
plt.title("Time it takes to check different midpoints \nfor each of the search tasks")
plt.legend()
plt.show()
