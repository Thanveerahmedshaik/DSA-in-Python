def rev_list(lst: list, left:int , right:int) -> list:
    """
    Reverse a list using recursion.
    
    :param lst: List to be reversed
    :return: Reversed list
    """
    if left >= right:
        return lst
    lst[left], lst[right] = lst[right], lst[left]
    return rev_list(lst, left + 1, right - 1)

# reverses a list using while loop
def rev_list_while(lst: list, left:int, right:int) -> list:
    """
    Reverse a list using a while loop.
    
    :param lst: List to be reversed
    :return: Reversed list
    """
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        return rev_list_while(lst, left+1, right-1)  # recursion still works
    return lst



# This function reverses a list using recursion.
# The time complexity is O(N) and 
# the space complexity is O(N) due to the recursion stack.


# Unit tests for the reverse list functions
import unittest

class TestReverseList(unittest.TestCase):
    def test_rev_list(self):
        self.assertEqual(rev_list([1, 2, 3, 4, 5], 0, 4), [5, 4, 3, 2, 1])
        self.assertEqual(rev_list([1], 0, 0), [1])
        self.assertEqual(rev_list([], 0, -1), [])

    def test_rev_list_while(self):
        self.assertEqual(rev_list_while([1, 2, 3, 4, 5], 0, 4), [5, 4, 3, 2, 1])
        self.assertEqual(rev_list_while([1], 0, 0), [1])
        self.assertEqual(rev_list_while([], 0, -1), [])


if __name__ == '__main__':
    unittest.main(exit=False)
    # Example usage
    original_list = [1, 2, 3, 4, 5]
    print("Original array:", original_list)
    reversed_list = rev_list(original_list.copy(), 0, len(original_list) - 1)
    print("Reversed array:", reversed_list)
    