# Counting the number of digits in an integer using logarithm
# Logic:

# The number of digits in a positive integer can be determined using the logarithm base 10.
# The formula is:
#   digits = floor(log10(n)) + 1  
# for example, for n = 12345:
#   log10(12345) = 4.09151498
#   floor(4.09151498) = 4
#   digits = 4 + 1 = 5  
from math import *
number = int(input("Enter a positive integer: "))
n = number
def count_digits(n):
    return floor(log10(n)) + 1 if n > 0 else 1

if number < 0:
    print("Please enter a positive integer.")
else:
    count = count_digits(n)
    print("The number of digits in", number, "is:", count)
# This code will correctly count the number of digits in a positive integer.
# If the input is negative, it prompts the user to enter a positive integer.  
# Note: The logarithm function is only defined for positive numbers, hence the check for positivity.
# This method is efficient and works well for large integers as well. 
# It avoids the need for loops and is more concise.
# Example usage:
# Enter a positive integer: 12345
# The number of digits in 12345 is: 5
# This method is particularly useful in competitive programming and scenarios where performance is critical.
# It leverages the mathematical properties of logarithms to provide a quick solution.



# Whats the time and space complexity of this code?
# If the iteration is done using a loop the time complexity is O(log 10 (n)) and space complexity is O(1).
# However, since we are using the logarithm function directly, the time complexity is O(1) and space complexity is also O(1).
# This is because the logarithm function computes the number of digits in constant time without needing to iterate through the digits of the number.
# Thus, the overall time complexity is O(1) and space complexity is O(1).

