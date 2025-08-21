from bubble_sort import Solution

def test_empty_list():
  assert Solution().bubble_sort([]) == []

def test_single_element():
  assert Solution().bubble_sort([5]) == [5]

def test_sorted_list():
  assert Solution().bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse_list():
  assert Solution().bubble_sort([3, 2, 1]) == [1, 2, 3]

def test_with_duplicates():
  assert Solution().bubble_sort([4, 1, 4, 2]) == [1, 2, 4, 4]

def test_negative_numbers():
  assert Solution().bubble_sort([-1, -3, 2, 0]) == [-3, -1, 0, 2]


def test_optimized_empty_list():
  assert Solution().bubble_sort_optimized([]) == []

def test_optimized_single_element():
  assert Solution().bubble_sort_optimized([5]) == [5]

def test_optimized_sorted_list():
  assert Solution().bubble_sort_optimized([1, 2, 3]) == [1, 2, 3]

def test_optimized_reverse_list():
  assert Solution().bubble_sort_optimized([3, 2, 1]) == [1, 2, 3]


