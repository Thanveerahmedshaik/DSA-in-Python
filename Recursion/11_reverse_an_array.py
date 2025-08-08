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


    
    