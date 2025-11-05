# Find the maximum subarray sum
# Given an integer array nums, find the contiguous subarray (containing at least one number
# which has the largest sum and return its sum.


from typing import List

class Solution: 
    """
    Kadane's Algorithm to find the maximum subarray sum in O(n) time.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        total = 0
        for i in range(0, n):
            total += nums[i]
            maxi = max(maxi, total)
            if total < 0:
                total = 0
        return maxi
# The time complexity of this approach is O(n) as it traverses the array once.
# The space complexity is O(1) as it uses a constant amount of space.


    