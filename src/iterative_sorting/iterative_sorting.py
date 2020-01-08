# TO-DO: Complete the selection_sort() function below 
# https://www.geeksforgeeks.org/selection-sort/
# takes the smallest element and moves to the smallest index available
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                #swap
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below

# Bubble sort, sometimes referred to as sinking sort, 
# is a simple sorting algorithm that repeatedly steps 
# through the list to be sorted, compares each 
# pair of adjacent items and swaps them if they are in the wrong order. 
# The pass through the list is repeated until no swaps are needed, 
# which indicates that the list is sorted.

def bubble_sort( arr ):
    #range(start, stop, step)
    #iterates starting at the end, stops at the beginning, steps by -1
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr