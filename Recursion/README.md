# 🔁 Recursion Algorithms in Python

## Overview

This folder contains recursive algorithm implementations that demonstrate the power of breaking down complex problems into simpler subproblems. Recursion is a fundamental concept in computer science, used in tree traversals, backtracking, divide-and-conquer algorithms, and more. Understanding recursion is crucial for solving many coding interview problems.

## Quick Run Instructions

To run any of the Python files in this folder, use the following command:

```bash
python3 filename.py
```

For example, to run the Fibonacci number calculation:

```bash
python3 13_fibonacci_number.py
```

Make sure you have Python 3 installed on your system. You can check by running:

```bash
python3 --version
```

## Problems/Algorithms

| File | Algorithm | Time Complexity | Space Complexity |
|------|-----------|----------------|------------------|
| [9_paramterized_recursion.py](9_paramterized_recursion.py) | Parameterized recursion technique | Depends on problem | Depends on problem |
| [10_Functional_recursion.py](10_Functional_recursion.py) | Functional recursion approach | Depends on problem | Depends on problem |
| [11_reverse_an_array.py](11_reverse_an_array.py) | Reverse an array using recursion | O(n) | O(n) |
| [12_string_palindrome.py](12_string_palindrome.py) | Check if string is palindrome using recursion | O(n) | O(n) |
| [13_fibonacci_number.py](13_fibonacci_number.py) | Calculate Fibonacci number recursively | O(2^n) | O(n) |

## Notes / Gotchas

- Recursion uses the call stack, so be mindful of stack overflow errors with deep recursion
- Every recursive function must have a base case to prevent infinite recursion
- Recursive solutions are often more readable but may be less efficient than iterative solutions
- For problems like Fibonacci, consider using memoization to optimize performance
- Tail recursion optimization is not performed by Python, unlike some other languages
- When debugging recursive functions, trace through a few simple cases to understand the flow

## Resources

- [GeeksforGeeks - Recursion](https://www.geeksforgeeks.org/recursion/)
- [Real Python - Recursion in Python](https://realpython.com/python-recursion/)
- [Backtracking Algorithms](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Python Maximum Recursion Depth](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit)
