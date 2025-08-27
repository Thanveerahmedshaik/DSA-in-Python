# right rotate the array by k places
def right_rotate_array_by_k_places(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    for i in range(k): 
        temp = arr[n-1] # Store the last element
        for j in range(n-2, -1, -1):
            arr[j+1] = arr[j] # Shift elements to the right
        arr[0] = temp # Place the last element at the front 
    return arr

# Optimal solution 

def rotate_array(array: list[int], k: int):
    n = len(array)
    k = k % n
    array[:] = array[n-k:] + array[:n-k]


# Time complexity is : O(n)
# Space complexity is : O(1) as it takes inplace
