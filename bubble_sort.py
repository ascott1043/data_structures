

def bubble_sort(elements):
    size = len(elements)
    iterations = 0


    for k in range(size - 1):
        swapped = False
        for i in range(size-1-k):   #Final elements are already sorted, so we skip those in each iteration
            iterations += 1
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True     
        
        if not swapped:
            break       #If sort iterates through entire list without swapping, then it's already sorted.  So we can break out of loop.

    print("Iterations: ", iterations)


def sort_dict(elements, key=None):
    size = len(elements)
    # if no key, pick first key from first dictionary
    if not key:
        key = list(elements[0])[0]

    for k in range(size - 1):
        swapped = False
        for i in range(size-1-k):
            if elements[i][key] > elements[i + 1][key]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                swapped = True    

        
        if not swapped:
            break  


if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements)
    print(elements)

    elements = [
        {'name':'kathy', 'amount':200, 'device':'vivo'},
        {'name':'dhaval', 'amount':400, 'device':'google pixel'},
        {'name':'amir', 'amount':600, 'device':'iphone-8'},
        {'name':'austin', 'amount':800, 'device':'iphone-10'}
    ]

    sort_dict(elements)
    print(elements)