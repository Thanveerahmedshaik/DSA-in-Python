from largest_element_in_array import solution

def test_largest_element():
    sol = solution()
    assert sol.largest_element([5, 11, 12, 22, 25, 34, 64, 90]) == 90
    assert sol.largest_element([-1, -5, -3, -4]) == -1
    assert sol.largest_element([0]) == 0
    assert sol.largest_element([1, 2, 3, 4, 5]) == 5
    assert sol.largest_element([-10, -20, -30, -5]) == -5


