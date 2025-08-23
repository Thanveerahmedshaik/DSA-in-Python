from typing import List

class solution():
    def if_array_sorted(self,nums : List[int]) ->bool:
        n = len(nums)
        for i in range(0,n-1):
            if nums[i]>nums[i+1]:
                return False

        return True



# time complexity is O(n) as it parses through the entire array once
# space complexity is O(1) as it uses a constant amount of space