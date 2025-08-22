from mergesort import Solution

def test_merge_sort_empty():
    assert Solution().merge_sort([]) == []

def test_merge_sort_single_element():
    assert Solution().merge_sort([5]) == [5]

def test_merge_sort_two_elements():
    assert Solution().merge_sort([5, 2]) == [2, 5]

def test_merge_sort_multiple_elements():
    assert Solution().merge_sort([5, 2, 9, 1]) == [1, 2, 5, 9]

def test_merge_sort_duplicates():
    assert Solution().merge_sort([5, 2, 2, 1]) == [1, 2, 2, 5]  

def test_merge_sort_negative_numbers():
    assert Solution().merge_sort([-1, -5, 2, 0]) == [-5, -1, 0, 2]

def test_merge_sort_sorted():
    assert Solution().merge_sort([1, 2, 3]) == [1, 2, 3]

def test_merge_sort_large_numbers():
    assert Solution().merge_sort([1000, 500, 10000, 0]) == [0, 500, 1000, 10000]    

def test_merge_sort_even_elements():
    assert Solution().merge_sort([8, 4, 2, 6]) == [2, 4, 6, 8]
