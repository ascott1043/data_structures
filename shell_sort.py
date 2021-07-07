import random

def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


def generate_test_arrays():
    #Generates randomized arrays of increasing lengths and then sorts them
    for i in range(10):
        new_array = []
        for x in range((i * 2)+1):
            new_array.append(random.randint(1, 1000))
        print("Length: ", len(new_array))
        print(new_array)
        shell_sort(new_array)
        print(new_array)
        print('\n')

if __name__ == '__main__':
    elements = [21,38,29,17,4,25,11,32,9]
    shell_sort(elements)
    print(elements)

    generate_test_arrays()

