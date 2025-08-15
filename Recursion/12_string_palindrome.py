def is_palindrome(s: str, left: int, right: int) -> bool:
    """
    Check if a string is palindrome or not

    :param s: The string to check
    :param left: The left index
    :param right: The right index
    :return: True if the string is a palindrome, False otherwise
    """
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)


# the time complexity of this function is O(N) where N is the length of the string, as it checks each character at most once.
# The space complexity is O(N) as well, due to the recursion stack. This is stack space used by the recursive calls.

def preprocess(s: str) -> str:
    # Remove spaces and convert to lowercase
    return ''.join(c.lower() for c in s if c.isalnum())

# Tests
def test_is_palindrome():
    assert is_palindrome("radar", 0, 4) == True
    assert is_palindrome("hello", 0, 4) == True, "Failed on 'hello'"
    assert is_palindrome("level", 0, 4) == True
    s = "A man a plan a canal Panama"
    s_clean = preprocess(s)
    assert is_palindrome(s_clean, 0, len(s_clean) - 1) == True

if __name__ == "__main__":
    try:
        test_is_palindrome()
        print("All tests passed!")
    except AssertionError as e:
        print("A test failed:", e)
