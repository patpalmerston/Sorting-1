# TO-DO: Complete the selection_sort() function below
'''
starting index / or current index
find smallest index in loop
swap the current index with the smallest
this happens for each iteration of the out loop
'''


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # this represents the sorted side of a "sub array", first index, a single index, is always sorted.
        min_index = i

        # inner loop runs against the outer loop plus 1, representing the unsorted part of the "sub array", looping against the single sorted starting index of the outer loop.
        for j in range(i+1, len(arr)):
            # if the inner loop index is less than the outer loop minimum then the minimum becomes the new lower valued index
            if arr[j] < arr[min_index]:
                min_index = j

        # every time we run to the end of the inner loop and have found a new minimum, we swap that minimum with the i index from the outer loop. Shifting the larger number into a new index position or the "unsorted sub array" for future looping

        # TO-DO: swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
