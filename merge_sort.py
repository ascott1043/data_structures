
import random
#My attempt, which surprisingly works:
def mergesort(arr):
    sorted = []
    if len(arr) > 1:
        middle = len(arr) // 2
        arr1 = mergesort(arr[0:middle])
        arr2 = mergesort(arr[middle::])

        while arr1 or arr2:
            if arr1 and arr2:
                if arr1[0] > arr2[0]:
                    sorted.append(arr2[0])
                    arr2.pop(0)
                else:
                    sorted.append(arr1[0])
                    arr1.pop(0)
            elif arr1:
                sorted.append(arr1[0])
                arr1.pop(0)
            elif arr2:
                sorted.append(arr2[0])
                arr2.pop(0)
    else:
        return arr
    return sorted

def generate_array(x=10):
    #generates random array of nbrs between 1-100 
    # that is X values long, default 10
    arr = []
    for i in range(x):
        arr.append(random.randint(1,100))
    return arr

#CodeBasics implementation, better than mine
# doesn't pop, better time complexity
#doesn't return additional arrays: better space complexity
def merge_two_sorted_lists(a, b, arr):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j+=1
        k += 1

    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
    

def merge_sort_codebasics(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort_codebasics(left)
    merge_sort_codebasics(right)

    merge_two_sorted_lists(left, right, arr)


if __name__ == '__main__':
    
    for i in range(1):
        a = generate_array(10)
        b = a
        print(a)
        print(mergesort(a))
        merge_sort_codebasics(b)
        print(b)
        print('\n')