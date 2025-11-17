class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        positive_index = 0
        negative_index = 1
        result = [0] * n

        for num in nums:
            if num > 0:
                result[positive_index] = num
                positive_index += 2
            else:
                result[negative_index] = num
                negative_index += 2
        return result
    
    # The time complexity of this approach is O(n) as it traverses the array once.
    # The space complexity is O(n) as it uses an additional array to store the result.

    
