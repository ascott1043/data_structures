import random

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end) #partition, returns index of corrected element
        quick_sort(elements, start, pi-1) #left partition
        quick_sort(elements, pi+1, end) #right partition


def generate_elements(int=5):
    #returns list of integers between 1 and 100
    elements = []
    for i in range(int):
        elements.append(random.randint(1,100))
    return elements



if __name__ == '__main__':
    for i in range(5):
        elements = generate_elements(6)

        print(elements)

        quick_sort(elements, 0, len(elements)-1)
        print(elements, '\n')
