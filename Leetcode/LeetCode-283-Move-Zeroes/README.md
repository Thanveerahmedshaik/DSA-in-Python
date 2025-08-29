# LeetCode 283: Move Zeroes  

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)  

**Link:** [Move Zeroes](https://leetcode.com/problems/move-zeroes/)  

---

## Problem Statement  
Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.  

You must do this **in-place** without making a copy of the array.  

---

### Example 1  
Input: nums = [0,1,0,3,12]  
Output: [1,3,12,0,0]  

### Example 2  
Input: nums = [0]  
Output: [0]  

---

## Constraints  
- 1 <= nums.length <= 10⁴  
- -2³¹ <= nums[i] <= 2³¹ - 1  

---

## Explanation of the Solution  

We use a **two-pointer technique**:  

1. **Pointer `j`** keeps track of the position where the next non-zero should be placed.  
2. We iterate through the array with index `i`.  
3. Whenever we see a non-zero, we swap it with `nums[j]`.  
   - This ensures that all non-zeros are moved to the left, maintaining order.  
4. Zeros automatically "move" to the right side of the array.  

This approach guarantees:  
- **Time Complexity:** O(n) — we scan the array once.  
- **Space Complexity:** O(1) — we only use a constant amount of extra memory.  

### Dry Run  
Input: `[0,1,0,3,12]`  

- i=0 → nums[0]=0 → skip  
- i=1 → nums[1]=1 → swap with nums[0] → `[1,0,0,3,12]`, j=1  
- i=2 → nums[2]=0 → skip  
- i=3 → nums[3]=3 → swap with nums[1] → `[1,3,0,0,12]`, j=2  
- i=4 → nums[4]=12 → swap with nums[2] → `[1,3,12,0,0]`, j=3  

Output: `[1,3,12,0,0]` ✅  

---

## Resources for Learning  
- [LeetCode Problem 283: Move Zeroes](https://leetcode.com/problems/move-zeroes/)  
- [Two Pointers Technique Explained (GeeksforGeeks)](https://www.geeksforgeeks.org/two-pointers-technique/)  
- [Python List Swapping Guide (Real Python)](https://realpython.com/python-swap-values/)  

---