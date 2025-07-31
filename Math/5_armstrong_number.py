# An Armstrong number (also known as a narcissistic number) is a number that is equal
# to the sum of its own digits each raised to the power of the number of digits(i.e, the length of the number).
# For example, 153 is an Armstrong number because:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# The code checks if the input number is an Armstrong number by calculating the sum of its digits raised to the power of the number of digits.
# If the sum equals the original number, it prints that the number is an Armstrong number; otherwise, it prints that it is not.

number = int(input("Enter a positive integer:"))

n = number
def is_armstrong(n):
    sum_of_powers = 0 
    num_digits = len(str(n)) # Count the number of digits
    original_number = n

    while n > 0:
        digit = n % 10
        sum_of_powers += digit ** num_digits
        n //= 10 # Removes the last digit from n

    return original_number == sum_of_powers

if is_armstrong(n):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# The time complexity of this code is O(log10(n)), where n is the input number, because we iterate through each digit once.
# The space complexity is O(1) since we are using a fixed amount of space(constant space) for variables regardless of the input size.
# This method is efficient and works well for checking Armstrong numbers of any size.
# Example usage:
# Enter a positive integer: 153
# 153 is an Armstrong number.
# Enter a positive integer: 123
# 123 is not an Armstrong number.
# This method is particularly useful in competitive programming and scenarios where performance is critical.    

