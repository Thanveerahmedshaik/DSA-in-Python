# Remove duplicates in a sorted array and return the number of unique elements

# Bruteforce Approach
def remove_duplicates_in_sorted_array_bruteforce(arr: list[int]) -> int:
  n = len(arr)
  if n == 0:
    return 0
  if n == 1:
    return 1
  frequency_map = {}
  for i in range(n):
    frequency_map[arr[i]] = frequency_map.get(arr[i],0) + 1
  unique_elements = 0
  for key in frequency_map:
    unique_elements += 1
  return unique_elements

# This function modifies the input array in-place
# Time Complexity: O(2n) simplified to O(n)
# The first loop iterates through the array to build the frequency map,
# and the second loop counts the unique elements.
# Space Complexity: O(n) as we store the frequency of each element.
# The frequency map will take up space proportional to the number of unique elements in the array.



# ***********************************************************************************************************************
# ***********************************************************************************************************************
# ***********************************************************************************************************************



# If the array is empty, we simply return 0, as there are no elements to process.
# Optimal Two Pointer Approach
def remove_duplicates_in_sorted_array(arr: list[int]) -> int:
  n = len(arr)
  i = 0 
  j = i + 1
  if n == 0:
    return 0
  if n == 1:
    return 1
  while j < n:
    if arr[i] != arr[j]:
      i += 1
      arr[i],arr[j] = arr[j],arr[i]
      j += 1
  return i+1

# Time complexity = O(n)
# Space Complexity = O(1)


# What we do in this approach is use two pointers to keep track of the unique elements.
# The first pointer `i` points to the last unique element found, and the second pointer `j` explores the array.
# Whenever we find a new unique element, we increment `i` and update the array in-place.
# This way, all unique elements are moved to the front of the array, 
# and we can easily determine the number of unique elements.
# What if the array is empty?
# If the array is empty, we simply return 0, as there are no elements to process.

