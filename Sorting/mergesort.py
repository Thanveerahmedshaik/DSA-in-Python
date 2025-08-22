class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_half = self.mergeSort(nums[:mid])
        right_half = self.mergeSort(nums[mid:])
        
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        sorted_array = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array