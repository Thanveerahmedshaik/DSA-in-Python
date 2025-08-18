from selection_sort import selection_sort

def test_empty_list():
    assert selection_sort([]) == []

def test_single_element():
    assert selection_sort([5]) == [5]

def test_sorted_list():
    assert selection_sort([1,2,3]) == [1,2,3]

def test_reverse_list():
    assert selection_sort([3,2,1]) == [1,2,3]

def test_with_duplicates():
    assert selection_sort([4,1,4,2]) == [1,2,4,4]