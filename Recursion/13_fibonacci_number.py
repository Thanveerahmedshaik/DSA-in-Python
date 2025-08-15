def fibonacci(n: int) -> int:
   """
   Calculate the nth Fibonacci number using recursion.
   :param n: The position in the fibonacci sequence
   :return: The fibonacci number at position n
   """
   if n == 0:
       return 0
   if n == 1:
       return 1
   return fibonacci(n - 1) + fibonacci(n - 2)

# The time complexity of this function is O(2^N) due to the two recursive calls.
# The space complexity is O(N) because the maximum depth of the recursion stack is N.




#Tests
def test_fibonacci():
   assert fibonacci(0) == 0 , "Failed on 0"
   assert fibonacci(1) == 1, "Failed on 1"
   assert fibonacci(2) == 1, "Failed on 2"
   assert fibonacci(3) == 2, "Failed on 3"
   assert fibonacci(4) == 3, "Failed on 4"
   assert fibonacci(5) == 5, "Failed on 5"
   assert fibonacci(6) == 8, "Failed on 6"
   assert fibonacci(7) == 13, "Failed on 7"
   assert fibonacci(8) == 21, "Failed on 8"
   assert fibonacci(9) == 34, "Failed on 9"
   assert fibonacci(10) == 55, "Failed on 10"

if __name__ == "__main__":
    try:
        test_fibonacci()
        print("All tests passed!")
    except AssertionError as e:
        print("A test failed:", e)
