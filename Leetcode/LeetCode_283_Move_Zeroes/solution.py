from typing import List

class Solution:
  def moveZeroes(self, nums) -> None:

    """
    :type nums: List[int]
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0 or len(nums) == 1:
      return
    j = 0 #Pointer for the next non-zero element
    for i in range(len(nums)):
      if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
    
# Time complexity is O(n) as it parses through the entire array once. 
# Space complexity is O(1) as it uses a constant amount of space.
