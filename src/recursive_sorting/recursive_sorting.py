# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    #Result Array
    arrC = []
    # TO-DO
    #while both array halves are not empty
    while len(arrA) != 0 and len(arrB) != 0:        
        if arrA[0] < arrB[0]: 
            arrC.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            arrC.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0:
        arrC += arrB
    else:
        arrC += arrA
    
    return arrC


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        #slices array from 0 index to half array
        arrA = merge_sort(arr[0:len(arr)//2])
        #slices array from half to end
        arrB = merge_sort(arr[len(arr)//2:])
        arr = merge(arrA, arrB)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
