# Merging two sorted arrays without duplicates

def merge_sort_single(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    # splitting the array into two halves
    mid = len(arr)//2
    left_half = merge_sort_single(arr[:mid])
    right_half = merge_sort_single(arr[mid:])
    return merge(left_half, right_half)

def merge_sort_two_arrays(arr1: list[int], arr2: list[int]) -> list[int]:

    sorted_arr1 = merge_sort_single(arr1)
    sorted_arr2 = merge_sort_single(arr2)
    return merge(sorted_arr1, sorted_arr2)
    

def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    merged = []
    leftIndex , rightIndex = 0, 0
    while leftIndex < len(arr1) and rightIndex < len(arr2):
        if arr1[leftIndex] < arr2[rightIndex]:
            if not merged or merged[-1] != arr1[leftIndex]:
                merged.append(arr1[leftIndex])
            leftIndex += 1
        elif arr1[leftIndex] > arr2[rightIndex]:
            if not merged or merged[-1] != arr2[rightIndex]:
                merged.append(arr2[rightIndex])
            rightIndex += 1
        else:
            if not merged or merged[-1] != arr1[leftIndex]:
                merged.append(arr1[leftIndex])
            leftIndex += 1
            rightIndex += 1

    while leftIndex < len(arr1):
        if not merged or merged[-1] != arr1[leftIndex]:
            merged.append(arr1[leftIndex])
        leftIndex += 1

    while rightIndex < len(arr2):
        if not merged or merged[-1] != arr2[rightIndex]:
            merged.append(arr2[rightIndex])
        rightIndex += 1

    return merged