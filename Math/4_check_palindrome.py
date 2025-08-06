# what is a palindrome?
# A palindrome is a word, phrase, number, or other sequence of characters that reads the
# same forward and backward (ignoring spaces, punctuation, and capitalization).
# For example, "madam", "racecar", and "12321" are palindromes.xsZX

number  =  int(input("Enter a number: "))
if isinstance(number, int):
# Check if the number is a palindrome
    n = number
    def is_palindrome(n):
      reversed_number = 0
      original_number = n
      while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n //= 10  # Removes the last digit from n example: 123 // 10 = 12

      return original_number == reversed_number
else: 
    print("Please enter a valid integer number.")

# The while loop iterates through the digits of the number, so it depends on the number of 
# digits in the number. The time complexity is O(log10(n)), where n is the input number.
# The number of constants is fixed and does not depend on the input size, so the space complexity is O(1).

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")