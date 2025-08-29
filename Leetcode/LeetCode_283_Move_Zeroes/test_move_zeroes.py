import pytest
from .solution import Solution



@pytest.mark.parametrize(
  "nums, expected",
  [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0,0,1], [1,0,0]),
    ([0], [0]),
    ([1,2,3], [1,2,3]),
    ([0,0,0], [0,0,0]),
    ([4,2,4,0,0,3,0,5,1,0], [4,2,4,3,5,1,0,0, 0,0]),  
    ([], []),
    ([1,0,1], [1,1,0])
  ]
)

def test_move_zeroes(nums, expected):
  arr = nums[:]
  ret = Solution().moveZeroes(arr)
  assert ret is None  # requires in-place modification, no return
  assert arr == expected


# What bugs this would catch:
# 1.Forgetting to move trailing zeros -> wrong expected comparison.
# 2.Accidentally returning a value -> ret is None fails.
# 3.Breaking order of non-zeros -> mismatch with expected.

def test_in_place_same_object():
  arr = [0,1,0,3,12]
  arr_id_before = id(arr)
  Solution().moveZeroes(arr)
  assert id(arr) == arr_id_before # To ensure the same object is modified in place

# Bug it catches:
# Accidentally creating and returning a new list instead of mutating the original.

def test_stable_order_of_non_zeros():
  arr = [0, 1, 0, 2, 0, 2, 1, 0, 3]
  nonzeros = [x for x in arr if x != 0]
  Solution().moveZeroes(arr)
  assert arr[:len(nonzeros)] == nonzeros  # Check the order of non-zero elements is preserved
  assert all(x == 0 for x in arr[len(nonzeros):])  # Check the rest are zeros

# What it’s proving:
# The relative order of non-zero items is unchanged (a key requirement).
# After placing all non-zeros at the front, everything after that is zero.

# Bug it catches:
# Any solution that shuffles non-zeros (e.g., unstable swaps or improper writes).