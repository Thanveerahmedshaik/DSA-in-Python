# Extraction of digits and reversing a number

number = int(input("Enter a number: "))

# Extract digits
digits = []
n = number
while n > 0:
  digit = n % 10
  digits.append(digit)
  n //= 10

print("Extracted digits (from least to most significant):", digits)

# Reverse the number
reversed_number = 0
n = number
while n > 0:
  digit = n % 10
  reversed_number = reversed_number * 10 + digit
  n //= 10

print("Reversed number:", reversed_number)


# Reversing the number using string manipulation
reversed_string = str(number)[::-1]
print("Revesing the number using string manipulation:", reversed_string)
# this method is more concise and leverages
# pythons string slicing capabilities.