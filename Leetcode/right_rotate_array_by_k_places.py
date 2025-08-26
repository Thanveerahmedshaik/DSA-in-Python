# right rotate the array by k places
def right_rotate_array_by_k_places(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    for i in range(k): 
        temp = arr[n-1] # Store the last element
        for j in range(n-2, -1, -1):
            arr[j+1] = arr[j] # Shift elements to the right
        arr[0] = temp # Place the last element at the front 
    return arr
# Test the function
print(right_rotate_array_by_k_places([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3]