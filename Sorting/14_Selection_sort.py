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


# Tests
print(selection_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]
print(selection_sort([5, 4, 3, 2, 1]))        # [1, 2, 3, 4, 5]
print(selection_sort([1, 2, 3, 4, 5]))        # [1, 2, 3, 4, 5]
print(selection_sort([]))                     # []