# Function to rotate the array by one place using slicing method

from typing import List

class solution():
    def rotate_array_by_one_slicing(arr: List[int]) -> List[int]:
        arr[:] = [arr[-1]] + arr[:-1]
        return arr
    # Time complexity using slicing is O(n) because we iterate through the entire array.
# Space complexity is O(n) because we because slicing and concatenation makes a new list.


# Function to rotate the array by one place using the traditional method
    def rotate_array_by_one(arr: List[int]) -> List[int]:
        if not arr:
            return arr  # Handle empty array

        last_element = arr[-1]  # Store the last element
        n = len(arr)

        # Shift elements to the right
        for i in range(n - 2, -1, -1):
            arr[i + 1] = arr[i]

        arr[0] = last_element  # Place the last element at the front
        return arr


# Time complexity using the traditional method is O(n) because we iterate through
# the entire list
# Space complexity is O(1) because we modify the array in place

