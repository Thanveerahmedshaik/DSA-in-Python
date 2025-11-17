import pytest
from Leetcode.LeetCode_2149_Rearrange_Array_Elements_By_Sign.rearrange_array_elements_by_sign import Solution 

@pytest.fixture

def sol():
    return Solution()


def test_basic_case(sol):
    nums = [3, 1, -2, -5, 2, -4]
    result = sol.rearrangeArray(nums)
    assert result[0] > 0 and result[1] < 0
    assert result == [3, -2, 1, -5, 2, -4]


def test_already_alternating(sol):
    nums = [1, -1, 2, -2, 3, -3]
    result = sol.rearrangeArray(nums)
    assert result == [1, -1, 2, -2, 3, -3]


def test_all_positives_first(sol):
    nums = [5, 8, 2, -1, -3, -6]
    result = sol.rearrangeArray(nums)
    assert result == [5, -1, 8, -3, 2, -6]


def test_all_negatives_first(sol):
    nums = [-4, -2, -6, 7, 1, 3]
    result = sol.rearrangeArray(nums)
    assert result == [7, -4, 1, -2, 3, -6]


def test_smallest_case(sol):
    nums = [1, -1]
    result = sol.rearrangeArray(nums)
    assert result == [1, -1]


def test_large_case(sol):
    nums = [10, -1, 20, -2, 30, -3, 40, -4]
    result = sol.rearrangeArray(nums)
    assert result == [10, -1, 20, -2, 30, -3, 40, -4]


def test_positions_are_correct(sol):
    nums = [4, -1, 5, -2, 6, -3]
    result = sol.rearrangeArray(nums)
    for i in range(0, len(result), 2):
        assert result[i] > 0     
    for i in range(1, len(result), 2):
        assert result[i] < 0    
    