Class Solution:
  def merge_sort(self, arr: List[int]) -> List[int]:
    if len(arr) > 1:
      mid = len(arr) // 2
      left_half = arr[:mid]
      right_half = arr[mid:]

      left_sorted = self.merge_sort(left_half)
      right_sorted = self.merge_sort(right_half)

      return self.merge(left_sorted, right_sorted)
    return arr

  def merge(self, left: List[int], right: List[int]) -> List[int]:
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        merged.append(left[i])
        i += 1
      else:
        merged.append(right[j])
        j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# The time complexity of merge sort is O(N log N) for all cases.
# The space complexity of merge sort is O(N) because it requires additional space for the temporary arrays.