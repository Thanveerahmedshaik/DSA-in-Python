# Find the largest element in array 
from typing import List

class solution:
  def largest_element(self, arr: List[int]) -> int:
    if not arr: # max([]) would normally raise a ValueError
      raise ValueError("Array is empty")
    largest_element = arr[0]
    for num in arr[1:]:
      if num > largest_element:
        largest_element = num
    return largest_element


# time complexity is O(n) as it parses through the entire array once
# space complexity is O(1) as it uses a constant amount of space

