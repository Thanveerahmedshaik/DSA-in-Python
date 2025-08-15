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
   return fibonnaci(n - 1) + fibonnaci(n - 2)


#Tests
def test_fibonacci():
   assert fibonnaci(0) == 0 , "Failed on 0"
   assert fibonnaci(1) == 1, "Failed on 1"
   assert fibonnaci(2) == 1, "Failed on 2"
   assert fibonnaci(3) == 2, "Failed on 3"
   assert fibonnaci(4) == 3, "Failed on 4"
   assert fibonnaci(5) == 5, "Failed on 5"
   assert fibonnaci(6) == 8, "Failed on 6"
   assert fibonnaci(7) == 13, "Failed on 7"
   assert fibonnaci(8) == 21, "Failed on 8"
   assert fibonnaci(9) == 34, "Failed on 9"
   assert fibonnaci(10) == 55, "Failed on 10"

if __name__ == "__main__":
    try:
        test_fibonacci()
        print("All tests passed!")
    except AssertionError as e:
        print("A test failed:", e)
