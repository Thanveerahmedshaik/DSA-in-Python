from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:

        """
        Brute-force O(n²) solution to find all index pairs adding up to target.
        """
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    the_indexes = [i, j]
                    result.append(the_indexes)
        return result
    
    def twoSumOptimized(self, nums: List[int], target: int) -> List[int]:

        """
        Return indices of the two numbers that add up to target using O(n) hash map.
        """
        hash_map = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hash_map:
                return[hash_map[remaining], i]
            hash_map[nums[i]] = i
        return []
    

# The time complexity of the brute-force approach is O(n^2) due to the nested loops.
# The optimized approach has a time complexity of O(n) because it traverses the list only once.
# The space complexity for the optimized approach is O(n) in the worst case, as we may store all elements in the hash map.  