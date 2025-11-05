# Test Cases for Maximum Subarray Sum Problem

import pytest
from Leetcode.LeetCode_53_Maximum_Subarray_Sum.max_subarray_sum import Solution

@pytest.fixture

def sol():
    return Solution()

def test_max_subarray_sum(sol):

    assert sol.maxSubArray([0]) == 0

    # Basic test cases
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5,4,-1,7,8]) == 23

    # Edge cases
    assert sol.maxSubArray([-1]) == -1
    assert sol.maxSubArray([-2,-3,-1,-5]) == -1
    assert sol.maxSubArray([0,0,0,0]) == 0

    # Larger array
    assert sol.maxSubArray([i for i in range(-1000, 1001)]) == sum(range(0, 1001))
    assert sol.maxSubArray([i if i % 2 == 0 else -i for i in range(1, 1001)]) == 1000
     

