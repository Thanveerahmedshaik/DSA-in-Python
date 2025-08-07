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

def test_reverse_list():
    lst = [1, 2, 3, 4, 5]
    print("Original List:", lst)
    reversed_lst = rev_list(lst, 0, len(lst) - 1)
    print("Reversed List:", reversed_lst)

# This function reverses a list using recursion.
# The time complexity is O(N) and 
# the space complexity is O(N) due to the recursion stack.

if __name__ == "__main__":
    test_reverse_list()
    