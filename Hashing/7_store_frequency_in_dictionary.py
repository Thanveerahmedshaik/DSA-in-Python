# Store frequency in a dictionary
# Lets say we have a list of numbers and we want to count the frequency of each number in the list


# Method 1: Using a dictionary to store frequency

# Example list of numbers 
# nums = [5,6,7,7,1,9,111,1,1,5,1,1]

def store_frequency_in_dictionary(nums):
    frequency_map = {}
    for i in range(len(nums)):
       if nums[i] in frequency_map:
           frequency_map[nums[i]] += 1
       else:
           frequency_map[nums[i]] = 1
    return frequency_map

# This function iterates through the list and counts the frequency of each number.
# If the number is already in the dictionary, it increments its count; otherwise, it initializes
# the count to 1.
# The final dictionary will contain each unique number as a key and its frequency as the value.
# The time complexity of this code is O(n), where n is the number of elements in the list,
# because we iterate though the list once.
# The space complexity in worst case is O(n) as well, since we may store all unique numbers in the dictionary.
# This method is efficient and works well for counting frequencies in large lists.



# Example usage:
# nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
# frequency_map = store_frequency_in_dictionary(nums)
# print(frequency_map)
# Output: {5: 2, 6: 1, 7: 2, 1: 5, 9: 1, 111: 1
# This method is particularly useful in data analysis and statistics where frequency counts are needed.
# It can be used in various applications such as counting occurrences of words in a text,
# analyzing survey results, or processing large datasets.


# Method 2: Using collections.Counter for frequency counting
# Counter is a built-in Python class from the collections module that returns a dictionary-like object.
# It counts how many times each element appears in a list (or any iterable).
# It gives the result as a dictionary-like object where:
#   keys = unique elements
#   values = how many times they occurred


from collections import Counter
def store_frequency_in_dictionary_with_counter(nums):
    frequency_map = Counter(nums) #return a dictionary like object with the frequency of each element
    return frequency_map
# This method uses the Counter class from the collections module to count the frequency of each number in the list.
# It is a more concise and efficient way to achieve the same result as the previous method.
# The time complexity is still O(n), but the implementation is cleaner and more readable.

# Example usage:
# nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
# frequency_map = store_frequency_in_dictionary_with_counter(nums)
# print(frequency_map)
# Output: Counter({1: 5, 5: 2, 7: 2, 6: 1, 9: 1, 111: 1})



# Method 3: HashMap for frequency counting
# A HashMap is a data structure that maps keys to values, allowing for fast retrieval of values based on keys.
# In Python, dictionaries are implemented as HashMaps.  

def store_frequency_in_dictionary_with_hashmap(nums):
    hash_map = {}
    n = len(nums)
    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
    return hash_map
# This method uses a HashMap (dictionary) to count the frequency of each number in the list.
# It uses the get method to retrieve the current count of the number, defaulting to 0 if the number is not already in the HashMap.
# It then increments the count by 1.
# The time complexity is O(n), where n is the number of elements in the list, as we iterate through the list once.
# The space complexity is O(n) in the worst case, as we may store all unique numbers in the HashMap.
# This method is efficient and works well for counting frequencies in large lists.


# Geeks for Geeks Problem Statement
"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        n = len(arr)
        hash_map = dict()
        for i in range(0,n):
            hash_map[arr[i]] = hash_map.get(arr[i],0)+1
        return hash_map[arr[x]]