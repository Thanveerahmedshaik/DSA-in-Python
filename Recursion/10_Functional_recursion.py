# Functional recursion example

import unittest

# This code demonstrates how to use functional recursion to compute the sum of n numbers.

def sum_recursion(n):
    if n== 0:
        return 0
    return n + sum_recursion(n-1)



# This code demonstrates how to use functional recursion to compute the factorial of a number n.

def factorial_recursion(n):
    if n == 1:
        return 1
    return n * factorial_recursion(n-1)


#test function to demonstrate the usage of the above functions

class TestRecursionFunctions(unittest.TestCase):
    def test_sum_recursion(self):
        self.assertEqual(sum_recursion(5), 15)
        self.assertEqual(sum_recursion(1), 1)
        self.assertEqual(sum_recursion(3), 6)
        self.assertEqual(sum_recursion(0), 0)

    def test_factorial_recursion(self):
        self.assertEqual(factorial_recursion(1), 1)
        self.assertEqual(factorial_recursion(5), 120)
        self.assertEqual(factorial_recursion(3), 6)
        self.assertEqual(factorial_recursion(2), 2)

if __name__ == '__main__':
    unittest.main()
