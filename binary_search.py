import random
import time


def native_search(list,target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
import time


def binary_search(list, target, left = None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(list) - 1
    # The target not in the list
    if right < left:
        return -1
    # Middle index of the list
    midpoint = (left + right) // 2
    if list[midpoint] == target:
        return midpoint
    elif list[midpoint] > target:
        return binary_search(list, target, left, midpoint -1)
    else:
        #list[midpoint] < target
        return binary_search(list, target, midpoint + 1 , right)


if __name__ =='__main__':
    
    length = int(input('Input length of list: '))
    print("Length of list:", length)
    list = set()
    #build a random list an then sorted it
    while len(list)  < length:
        # Add random int number in range (-length, length)
        list.add(random.randint(-length, length))
    sorted_list =sorted(list)

    start = time.time()
    #Search every element in sorted_list
    for target in sorted_list:
        native_search(sorted_list,target)
    end = time.time()
    print("Native search time: ", (end - start) / length, "seconds")

    start = time.time()
    #Search every element in sorted_list
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")