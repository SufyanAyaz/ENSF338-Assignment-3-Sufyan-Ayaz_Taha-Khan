import heapq
import time
import random
import numpy as np
import matplotlib.pyplot as plt


def inefficient_insertion_extraction_priority_queue(values):
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[j] < values[i]:
                values[i], values[j] = values[j], values[i]
    result = []
    while values:
        result.append(heapq.heappop(values))
    return result


def efficient_insertion_extraction_priority_queue(values):
    heap = list(values)
    heapq.heapify(heap)
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result


def measure_time(function, input_data):
    start_time = time.time()
    function(input_data)
    return time.time() - start_time


def run_experiment(input_size):
    inputs = list(range(input_size))
    random.shuffle(inputs)
    measurements_inefficient = []
    measurements_efficient = []
    num_measurements = 100
    for i in range(num_measurements):
        measurement_inefficient = measure_time(
            inefficient_insertion_extraction_priority_queue, list(inputs))
        measurement_efficient = measure_time(
            efficient_insertion_extraction_priority_queue, inputs)
        measurements_inefficient.append(measurement_inefficient)
        measurements_efficient.append(measurement_efficient)
    print("Inefficient: min={}, avg={}".format(
        np.min(measurements_inefficient), np.mean(measurements_inefficient)))
    print("Efficient: min={}, avg={}".format(
        np.min(measurements_efficient), np.mean(measurements_efficient)))
    plt.hist(measurements_inefficient, alpha=0.5, label='Inefficient')
    plt.hist(measurements_efficient, alpha=0.5, label='Efficient')
    plt.xlabel(
        'Time taken for extraction and insertion from priority queue (seconds)')
    plt.ylabel('Frequency count')
    plt.title(
        'Comparison of inefficient and efficient priority queue implementation')
    plt.legend(loc='upper right')
    plt.show()


run_experiment(1000)
