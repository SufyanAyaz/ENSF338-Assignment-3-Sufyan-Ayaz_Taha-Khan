import timeit

import matplotlib.pyplot as plt


def search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


def binary_search(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


input_list = list(range(1000))

linear_search_time = timeit.timeit(
    "search(input_list, 999)", globals=globals(), number=1000)
print("Linear search execution time: {:.6f} seconds".format(
    linear_search_time))

binary_search_time = timeit.timeit(
    "binary_search(input_list, 999)", globals=globals(), number=1000)
print("Binary search execution time: {:.6f} seconds".format(
    binary_search_time))

linear_search_times = []
binary_search_times = []

for i in range(100):
    linear_search_time = timeit.timeit(
        "search(input_list, 999)", globals=globals(), number=1000)
    binary_search_time = timeit.timeit(
        "binary_search(input_list, 999)", globals=globals(), number=1000)
    linear_search_times.append(linear_search_time)
    binary_search_times.append(binary_search_time)

plt.hist(linear_search_times, alpha=0.5, label='Linear Search')
plt.hist(binary_search_times, alpha=0.5, label='Binary Search')
plt.xlabel('Execution time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

print("Average execution time for linear search: {:.6f} seconds".format(
    sum(linear_search_times) / len(linear_search_times)))
print("Average execution time for binary search: {:.6f} seconds".format(
    sum(binary_search_times) / len(binary_search_times)))
