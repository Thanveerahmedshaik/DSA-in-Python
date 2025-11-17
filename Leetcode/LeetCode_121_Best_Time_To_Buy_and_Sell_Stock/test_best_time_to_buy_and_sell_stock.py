#Test cases

# Test Cases for Best Time to Buy and Sell Stock Problem
import pytest
from Leetcode.LeetCode_121_Best_Time_To_Buy_and_Sell_Stock.best_time_to_buy_and_sell_stock import Solution

@pytest.fixture
def sol():
    return Solution()

def test_increasing(sol):
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4

def test_decreasing(sol):
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

def test_single_element(sol):
    assert sol.maxProfit([5]) == 0

def test_empty_array(sol):
    assert sol.maxProfit([]) == 0

def test_standard_case(sol):
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

def test_profit_late(sol):
    assert sol.maxProfit([5, 4, 3, 2, 1, 10]) == 9

def test_duplicates(sol):
    assert sol.maxProfit([2, 2, 2, 2, 3]) == 1

def test_peak_early(sol):
    assert sol.maxProfit([10, 9, 8, 7, 11]) == 4

def test_random_fluctuations(sol):
    assert sol.maxProfit([3, 8, 2, 5, 10, 1, 7]) == 8
