import pytest
from solution import Solution

@pytest.fixture
def sol():
    return Solution()

def test_missing_number(sol):
    # Normal cases
    assert sol.missingNumber([3,0,1]) == 2
    assert sol.missingNumber([0,1]) == 2
    assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert sol.missingNumber([0,2]) == 1

    ## Edge cases
    assert sol.missingNumber([0]) == 1
    assert sol.missingNumber([1]) == 0
    assert sol.missingNumber([]) == 0
def test_missing_number_xor(sol):
    # Normal cases
    assert sol.missingNumber([3,0,1]) == 2
    assert sol.missingNumber([0,1]) == 2
    assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert sol.missingNumber([0,2]) == 1

    ## Edge cases
    assert sol.missingNumber([0]) == 1
    assert sol.missingNumber([1]) == 0
    assert sol.missingNumber([]) == 0 


