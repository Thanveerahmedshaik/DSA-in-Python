# Find the missing number in an array
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    # Alternative approach using XOR
    def missingNumberXOR(self, nums: list[int]) -> int:
        n = len(nums)
        xor_all = 0
        xor_array = 0
        
        for i in range(n + 1):
            xor_all ^= i
            
        for num in nums:
            xor_array ^= num
            
        return xor_all ^ xor_array
    


# The time complexity for Xor approach is O(n + n) = O(n) and space complexity is O(1)
# The time complexity for Sum approach is O(n) and space complexity is O(1)
