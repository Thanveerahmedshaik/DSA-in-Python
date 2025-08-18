def selection_sort(arr: list[int]) -> list[int]:
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


