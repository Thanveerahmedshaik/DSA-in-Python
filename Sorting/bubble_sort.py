from typing import List
class Solution:
  def bubble_sort(self, arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n-2, -1, -1):
      for j in range(0, i+1):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
  
  def bubble_sort_optimized(self, arr: List[int]) -> List[int]:
    
      n= len(arr)
      for i in range(n-2,-1,-1):
        swapped=False
        for j in range(0,i+1):
          if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j]
            swapped = True
        if swapped == False:
          break
      return arr
