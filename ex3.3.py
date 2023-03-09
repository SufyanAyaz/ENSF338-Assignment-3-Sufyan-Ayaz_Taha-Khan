import sys

capacity_testing_list = []
capacity_of_list = sys.getsizeof(capacity_testing_list)

for element in range(64):
    capacity_testing_list.append(element)
    updated_capacity_of_list = sys.getsizeof(capacity_testing_list)
    if updated_capacity_of_list != capacity_of_list:
        print(
            f'Capacity has changed! The capacity has changed from {capacity_of_list} to {updated_capacity_of_list}')
        capacity_of_list = updated_capacity_of_list
    element += 1
