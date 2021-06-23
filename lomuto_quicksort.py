

def swap(start, end, elements):
    if start != end:
        elements[start],elements[end] = elements[end],elements[start]

def quicksort(elements, start, end):
    if len(elements) <= 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quicksort(elements, start, pi-1) #left partition
        quicksort(elements, pi+1, end) #right partition

"""
My attempt, which failed:  

def partition(elements, start, end):
    pivot_index = end
    partition_index = start
    pivot = elements[pivot_index]

    while partition_index < pivot_index:
        while pivot >= elements[partition_index] and partition_index < len(elements):
            partition_index += 1
        i = partition_index
        while pivot < elements[i] and i < len(elements):
            i += 1
        if partition_index < i:
            swap(partition_index, i, elements)

    swap(partition_index, pivot_index, elements)
    return end"""

def partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index





if __name__ == '__main__':
    elements  = [11,9,14,12,54,23]

    quicksort(elements, 0, len(elements) - 1)
    print(elements)