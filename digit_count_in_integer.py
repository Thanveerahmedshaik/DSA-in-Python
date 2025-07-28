# Question is you will be given an integer and you have to count the number of digits in it.


# Count the number of digits in an integer
number = int(input("Enter an integer: "))
count = 0
n = number
while n>0:
  n//=10
  count += 1
  

print("The number of digits in", number, "is:", count)
# If the number is 0, it has 1 digit

if number == 0:
  count = 1
  print("The number of digits in", number, "is:", count)
# This is because 0 is a single digit number.
# The while loop continues until n becomes 0, incrementing the count for each digit.
# The final count is printed, which represents the number of digits in the integer.
# If the input is negative, the absolute value is considered for counting digits.
# This is because the number of digits is independent of the sign.

# Note: If you want to handle negative numbers, you can take the absolute value of the number before counting digits.
# Example: If the input is -12345, the output will still be 5.  
# This is because the number of digits is independent of the sign.
# If you want to count the digits in a negative number, you can modify the code as follows:
if number < 0:
  number = abs(number)
  count = 0
  n = number
  while n > 0:
    n //= 10
    count += 1
  print("The number of digits in", number, "is:", count)
# This will ensure that the count is accurate regardless of the sign of the input number.
# This is useful for applications where the sign of the number is not relevant to the digit count
# such as in data analysis or statistics.   
