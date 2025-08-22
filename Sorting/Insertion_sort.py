from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr



#time complexity for this algorithm is O(N^2) in the worst and average cases.
#space complexity is O(1) since it sorts the array in place without using any additional data structures.

list_to_sort = [12, 11, 13, 5, 6]
sorted_list = insertion_sort(list_to_sort)
print("Sorted array is:", sorted_list)