from typing import List


class solution():
    def second_largest_element(nums : List[int]) -> int:
        n = len(nums)
        largest = float('-inf')
        second_largest = float ('-inf')

        for i in range(0,n):
            if nums[i]>largest:
                second_largest = largest
                largest = nums[i]

            elif nums[i]>second_largest and nums[i] != largest:
                second_largest = nums[i]

        return second_largest
    

# time complexity is O(n) as it parses through the entire array once
# space complexity is O(1) as it uses a constant amount of space




