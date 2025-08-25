from remove_duplicates_in_a_sorted_array import solution

def test_remove_duplicates():
    assert solution.remove_duplicates_in_sorted_array_bruteforce([1, 1, 2]) == 2

def test_remove_duplicates2():
    assert solution.remove_duplicates_in_sorted_array([0,0,1,1,1,2,2,3,3,4]) == 5


