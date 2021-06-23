import random
from util import time_it

@time_it
def linear_search(nbrs, nbr_to_find):
    iterations = 0
    for index, element in enumerate(nbrs):
        iterations += 1
        if element==nbr_to_find:
            return (index, iterations)
    return (-1, iterations)

@time_it
def binary_search(nbrs, nbr_to_find):
    left_index = 0
    right_index = len(nbrs) - 1
    mid_index = 0
    iterations = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_nbr = nbrs[mid_index]
        iterations += 1

        if mid_nbr == nbr_to_find:
            return (mid_index, iterations)

        if mid_nbr < nbr_to_find:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return (-1, iterations)

def binary_search_recursive(nbrs, nbr_to_find, left_index, right_index, iterations=1):
    if right_index < left_index:
        return (-1, iterations)

    mid_index = (left_index + right_index) // 2
    mid_nbr = nbrs[mid_index]

    if mid_index >= len(nbrs) or mid_index < 0:
        return -1

    if mid_nbr == nbr_to_find:
        return (mid_index, iterations)
    if mid_nbr < nbr_to_find:
        left_index = mid_index + 1
    if mid_nbr > nbr_to_find:
        right_index = mid_index - 1

    index, iterations = binary_search_recursive(nbrs, nbr_to_find, left_index, right_index, iterations+1)

    return (index, iterations)

@time_it
def multiple_indexes(nbrs, nbr_to_find):
    left_index = 0
    right_index = len(nbrs) - 1
    mid_index = 0

    while right_index >= left_index:
        mid_index = (right_index + left_index) // 2
        mid_nbr = nbrs[mid_index]

        if mid_nbr == nbr_to_find:
            right = find_right(nbrs, mid_index, [])
            left = find_left(nbrs, mid_index, [])
            indexes = left + [mid_index] + right

            #return as int instead of list if there is just one value
            if len(indexes) == 1:
                return indexes[0]
            return indexes

        if mid_nbr > nbr_to_find:
            right_index = mid_index - 1
        if mid_nbr < nbr_to_find:
            left_index = mid_index + 1

def find_right(nbrs, mid_index, indexes): #nbrs, 6, [6]
    mid_nbr = nbrs[mid_index]
    next_index = mid_index + 1
    while nbrs[next_index] == mid_nbr:

        indexes.append(next_index)
        next_index += 1

    return indexes          

def find_left(nbrs, mid_index, indexes):

    mid_nbr = nbrs[mid_index]
    next_index = mid_index - 1
    while nbrs[next_index] == mid_nbr:
        indexes.append(next_index)
        next_index -= 1

    return indexes


if __name__ == '__main__':
    # nbrs = [12, 15, 17, 19, 21, 24, 45, 67]
    # nbr_to_find = 15

    nbrs = [i for i in range(1000000)]
    nbr_to_find = random.randint(1,1000000)

    print("Random nbr: ", nbr_to_find)
    print(linear_search(nbrs, nbr_to_find))

    print(binary_search(nbrs, nbr_to_find))
    print("recursive: ", binary_search_recursive(nbrs, nbr_to_find, 0, len(nbrs)))

    nbrs = [1, 4, 6, 9,11,15,15,15,17,21,34,34,56]
    nbr_to_find = 15

    print(multiple_indexes(nbrs, nbr_to_find))