# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # find the length of the arrays combined
    elements = len(arrA) + len(arrB)
    # create an array with the number of index equal to the length of elements
    merged_arr = [0] * elements
    # create variable counters, one for the left, one for the right and one for the merged_arr. They will be used to match our looped index's to the merged array index count
    i = j = k = 0
    # while the i and j counters are less then the length of the arrays
    while i < len(arrA) and j < len(arrB):
      # if left is less than the right
        if arrA[i] < arrB[j]:
          # the merged_arr array index is equal to the lesser valued index
            merged_arr[k] = arrA[i]
            # increment i to keep track of the index relative to the left array and the index being looped
            i += 1
        else:
          # the merged_arr array index is equal to the lesser valued index
            merged_arr[k] = arrB[j]
            # incrment j to keep track of the index relative to the right array and the index being looped
            j += 1
        # for every i or j index, k needs to be iterated to keep track of the number of indexes in the final array
        k += 1
    # if either array only has one index, this will default add it to the end of the array as it will be the largest valued index left
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    # return the final array
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # base case to make sure the list has at least one index
    if len(arr) <= 1:
        return arr

    # find the mid point (what does // do?)
    mid = len(arr) // 2
    # inside a recursive call, slice blank to mid, is default(zero index to the mid point)
    left = merge_sort(arr[:mid])
    # inside a recursive call, slice from mid to blank, is default(mid to end of list)
    right = merge_sort(arr[mid:])
    # return and sort the recursively seperated arrays
    return merge(left, right)


# Version 2
# def merge(left, right):
#   # 4 variables, 1 list 3 counters, a counter for each loop, and counter for result list

#   i, j = 0, 0
#   result = []
#   #loop until i or j is larger equal to the length of the lists
#   while i < len(left) and j < len(right):
#   # if value of left is less than the value of right append the lower value to result
#     if left[i] < right[j]:
#       result.append(left[i])
#       # increment i so we stay within the while loop condition
#       i+=1
#   # else the lesser value is on the right
#     else:
#       result.append(right[j])
#       # increment i so we stay within the while loop condition
#       j+=1
#   # for any single indexed list default to add them to the end of the list
#   result += left[i:]
#   result += right[j:]
#   # return result
#   return result


# def merge_sort(arr):
#   #need a Base
#   if len(arr) <= 1:
#       return arr
#   # need to find the min
#   mid = len(arr) // 2
#   # slice the beginning
#   left = merge_sort(arr[:mid])
#   # slice the end
#   right = merge_sort(arr[mid:])
#   # merge with helper function
#   # print(left, right)

#   return merge(left, right)

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
