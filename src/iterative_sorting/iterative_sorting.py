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
# needs to be refactored for performance
def bubble_sort(arr):
    # outer loop
    for i in range(len(arr)):
        # pointer starts at the zero index
        left = i
        # inner loop
        for j in range(i+1, len(arr)):
            # pointer starts at the second index
            right = j
            # if the left index is larger than the right = swap
            if arr[right] < arr[left]:
                # swap
                arr[right], arr[left] = arr[left], arr[right]
    # return array
    return arr

# using a outer loop in revers and an inner loop going forward:

# def bubble_sort(arr):
#     for i in range(-1, len(arr)):
#         # print(arr[i])
#         right = i
#         for j in range(len(arr)):
#             print(arr[i], arr[j])
#             left = j

#             if arr[left] > arr[right]:
#             arr[left], arr[right] = arr[right], arr[left]
#     return arr

# b_list = [4,3,5,9,1,6]
# print(bubble_sort(b_list))


# Insertion sort
def insertion_sort(arr):
    # -insertion sort seperates the array into sorted and unsorted
    # -do this by looping through the array skipping the initial Value
    # -that value is the sorted side
    for i in range(1, len(arr)):
        # -we will need a variable that is the current value of the looped index
        # -we will need another variable j equal to the index of the outer loop
        # -we will bounce off the 'current' variable with j-1 to check the sorted side
        current = arr[i]
        j = i
# -we can only loop the inner loop if the index of j is greater than zero(meaning the index is greater than zero) and only if current is less than the value of the sorted side arr[j-1]
        while j > 0 and current < arr[j-1]:
            # -if that is true than we need arr[j] = arr[j-1] / this moves the greater value forward one Index
            arr[j] = arr[j-1]
# --then we decrement J so that we will continue to loop backwards to check for greater value vs the value of current, per the conditional in the loop statement
            j -= 1
# -in the outer loop scope we then change the current loop index of J to be the current Value which was the lesser value, placeing it before the greater value that was arr[j-1]
        arr[j] = current

    return arr

    '''
        with bubble we need two pointers, left index and right index that increment forward together
        left starts at 0 index, right starts at 1
        Outer loop starts with our 0 index
        inner loop starts with our second index
        as we run the inner loop against the outer loop we check to see if the j index is less than i. if it is then we swap and return arr

        '''


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
