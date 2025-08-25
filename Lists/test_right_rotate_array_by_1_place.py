from right_rotate_array_by_1_place import solution

def test_rotate_array_by_one():
    assert solution.rotate_array_by_one([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]

def test_rotate_array_by_one_empty():
    assert solution.rotate_array_by_one([]) == []

def test_rotate_array_by_one_single():
    assert solution.rotate_array_by_one_slicing([1]) == [1]

def test_rotate_array_by_one_multiple_elements():
    assert solution.rotate_array_by_one_slicing([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]