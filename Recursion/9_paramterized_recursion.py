# Parameterized Recursion
# This file demonstrates the concept of parameterized recursion in Python.

# Head Recursion 
# print 1 to N using recurssion
def head_recursion(i, N):
    if i > N:
        return
    print(i)
    head_recursion(i + 1, N)
# This function prints numbers from 1 to N using head recursion.

def tail_recursion(N, i):
    if i > N:
        return
    tail_recursion(N-1,i)
    print(N)

# the time complexity of this function is O(N+1) which is approximately equal to O(N) because it makes N recursive calls, and each call takes O(1) time.
# The space complexity is O(N+1) which is approximately equal to O(N) due to the recursion stack.



def test_parameterized_recursion():
    N = 5
    print("Head Recursion:")
    head_recursion(1, N)
    
    print("\nTail Recursion:")
    tail_recursion(N,1)

test_parameterized_recursion()


import unittest
from io import StringIO
import sys
import importlib

# Dynamically import the module since its name starts with a digit
mod = importlib.import_module("9_paramterized_recursion")

class TestParameterizedRecursion(unittest.TestCase):
    def test_head_recursion(self):
        output = StringIO()
        sys.stdout = output
        mod.head_recursion(1, 5)
        sys.stdout = sys.__stdout__
        result = output.getvalue().strip().split('\n')
        expected = ['1', '2', '3', '4', '5']
        self.assertEqual(result, expected)

    def test_tail_recursion(self):
        output = StringIO()
        sys.stdout = output
        mod.tail_recursion(5, 1)
        sys.stdout = sys.__stdout__ 
        result = [line for line in output.getvalue().strip().split('\n') if line]
        expected = ['1', '2', '3', '4', '5']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()