# n = [5,4,2,2,1,1,1,1,3,3,3,3,3,3,3,3] #prestore

# m = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

# Brute force method
def store_frequency_brute_force(nums, m):
    
    for num in m:
        count = 0
        for i in nums:
            if i == num:
                count += 1
        print("Frequency of", num, "is", count)

# Time complexity: O(n*m) where n is the length of n and m is the length of m
# In worst case, we have to iterate through the entire list n for each element in m.
# Space complexity: O(1) since we are not using any additional data structures that grow with input size.

# Using hashlist

def store_frequency_hashlist(nums, m):
    
    hash_list =  [0] * (max(nums) + 1)  # Create a hash list with size max(nums) + 1
    for i in nums:
        hash_list[i] += 1
    for num in m:
        if num <1 or num > max(nums):
            print("Frequency of", num, "is 0")
        else:
            print("Frequency of", num, "is", hash_list[num])

# Time complexity: O(n + m) where n is the length of nums and m is the length of m
# We iterate through nums once to build the hash list and then through m to get frequencies.
# Space complexity: O(max(nums)) since we are using a hash list of size max(nums) + 1.

def store_frequency_dictionary(nums, m):
    hash_dict = {}
    for i in nums:
        hash_dict[i] = hash_dict.get(i, 0) + 1
    for num in m:
        if num < 1 or num > max(nums):
            print("Frequency of", num, "is 0")
        else:
            print("Frequency of", num, "is", hash_dict.get(num, 0))

# Time complexity: O(n + m) where n is the length of nums and m is the length of m
# We iterate through nums once to build the hash dictionary and then through m to get frequencies.
# Space complexity: O(n) where n is the number of unique elements in nums,
# since we store each unique element as a key in the dictionary in worst case.

s = "azbcdnnnnsxkkgld"
q = ['a', 'b', 'c', 'd', 'n', 's', 'x', 'k', 'g', 'l']
def store_frequency_string(s, q):
    frequency_map = {}
    for char in s:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    for char in q:
        print(f"Frequency of '{char}' is {frequency_map.get(char, 0)}")






