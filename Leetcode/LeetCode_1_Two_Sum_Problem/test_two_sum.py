import pytest
from Leetcode.LeetCode_1_Two_Sum_Problem.two_sum_solution import Solution

@pytest.fixture
def sol():
    return Solution()

# ---------------------------
# Brute Force Tests
# ---------------------------
def test_two_sum_basic(sol):
    assert [0, 1] in sol.twoSum([2, 7, 11, 15], 9)

def test_two_sum_multiple_pairs(sol):
    result = sol.twoSum([1, 2, 3, 4, 5, 6], 7)
    expected = [[0, 5], [1, 4], [2, 3]]
    assert sorted(result) == sorted(expected)

def test_two_sum_empty(sol):
    assert sol.twoSum([], 5) == []

def test_two_sum_no_match(sol):
    assert sol.twoSum([1, 2, 3], 10) == []

# ---------------------------
# Optimized Tests
# ---------------------------
def test_two_sum_optimized_basic(sol):
    assert sol.twoSumOptimized([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_optimized_with_duplicates(sol):
    assert sol.twoSumOptimized([3, 3], 6) == [0, 1]

def test_two_sum_optimized_no_match(sol):
    assert sol.twoSumOptimized([1, 2, 3], 10) == []

def test_two_sum_optimized_negative_numbers(sol):
    assert sol.twoSumOptimized([-3, 4, 3, 90], 0) == [0, 2]
