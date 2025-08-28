# 🧮 Math Algorithms in Python

## Overview

This folder contains Python implementations of common mathematical algorithms and number theory problems. These are fundamental concepts often used in competitive programming and technical interviews. The problems here help build a strong foundation in mathematical problem-solving.

## Quick Run Instructions

To run any of the Python files in this folder, use the following command:

```bash
python3 filename.py
```

For example, to run the digit extraction and number reversing program:

```bash
python3 1_digit_extaction_and_reversing_number.py
```

Make sure you have Python 3 installed on your system. You can check by running:

```bash
python3 --version
```

## Problems/Algorithms

| File | Algorithm | Time Complexity | Space Complexity |
|------|-----------|----------------|------------------|
| [1_digit_extaction_and_reversing_number.py](1_digit_extaction_and_reversing_number.py) | Digit extraction and number reversal | O(d) where d is number of digits | O(1) |
| [2_digit_count_in_integer.py](2_digit_count_in_integer.py) | Count digits in an integer | O(d) where d is number of digits | O(1) |
| [3_digit_count_logarithm.py](3_digit_count_logarithm.py) | Count digits using logarithm | O(1) | O(1) |
| [4_check_palindrome.py](4_check_palindrome.py) | Check if a number is palindrome | O(d) where d is number of digits | O(1) |
| [5_armstrong_number.py](5_armstrong_number.py) | Check if a number is Armstrong number | O(d) where d is number of digits | O(1) |
| [6_factors_of_a_number.py](6_factors_of_a_number.py) | Find all factors of a number | O(√n) | O(1) |

## Notes / Gotchas

- When working with large numbers, be aware of potential integer overflow issues in other languages (not typically an issue in Python)
- For digit manipulation problems, remember that modulo (%) and integer division (//) are your key tools
- The logarithm method for counting digits is faster but requires importing the math module
- Armstrong numbers are numbers where the sum of their digits raised to the power of the number of digits equals the number itself

## Resources

- [GeeksforGeeks - Mathematical Algorithms](https://www.geeksforgeeks.org/mathematical-algorithms/)
- [Number Theory for Programming](https://www.geeksforgeeks.org/number-theory-competitive-programming/)
- [Python Math Module Documentation](https://docs.python.org/3/library/math.html)
