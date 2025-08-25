# Linear search an element k with given list n

from typing import List

class solution():
    def linear_search(n: List[int], k: int) -> int:
        l = len(n)
        for i in range(0, l):
            if n[i] == k:
                return i


# time complexity is O(n) as it may need to check every element in the list
# space complexity is O(1) as it uses a constant amount of space