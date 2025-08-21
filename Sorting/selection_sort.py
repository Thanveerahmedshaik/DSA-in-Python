from typing import List

def selection_sort(arr: List[int]) -> List[int]:
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr


# The time complexity of selection sort is O(N(N+1)/2) which is O(N^2) in the worst and average cases.
# The space complexity is O(1) since it sorts the array in place without using any additional data structures.


def selection_sort_desc(arr: List[int]) -> List[int]:
  n = len(arr)
  for i in range(n):
    max_index = i
    for j in range(i + 1, n):
      if arr[j] > arr[max_index]:
        max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]
  return arr


# the time complexity of selection sort is O(N(N+1)/2) which is O(N^2) in the worst and average cases.
# the space complexity is O(1) since it sorts the array in place without using any additional data structures.