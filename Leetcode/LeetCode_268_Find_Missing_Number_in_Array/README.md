# LeetCode 268: Missing Number  

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)  

**Link:** [Missing Number](https://leetcode.com/problems/missing-number/)  

---

## Problem Statement  
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the **only number** in the range that is missing from the array.  

You are asked to solve it **in O(n) time** and using **O(1) extra space**.  

---

### Example 1  
Input: nums = [3,0,1]  
Output: 2  
**Explanation:** n = 3, so numbers should be in range [0,3]. 2 is missing.  

### Example 2  
Input: nums = [0,1]  
Output: 2  
**Explanation:** n = 2, so numbers should be in range [0,2]. 2 is missing.  

### Example 3  
Input: nums = [9,6,4,2,3,5,7,0,1]  
Output: 8  
**Explanation:** n = 9, so numbers should be in range [0,9]. 8 is missing.  

---

## Constraints  
- `n == nums.length`  
- `1 <= n <= 10⁴`  
- `0 <= nums[i] <= n`  
- All the numbers of `nums` are **unique**  

---

## Explanation of the Solution  

We can use the **sum formula** or **XOR technique** for O(1) space:  

### Method 1: Using Sum Formula  
1. The sum of numbers from `0` to `n` is `total = n*(n+1)/2`.  
2. Subtract the sum of the array from `total`.  
3. The difference is the missing number.  

**Time Complexity:** O(n) — we iterate through the array once.  
**Space Complexity:** O(1) — no extra space needed.  

### Method 2: Using XOR  
1. XOR all numbers from `0` to `n` → `xor_total`.  
2. XOR all numbers in `nums` → `xor_array`.  
3. Missing number = `xor_total ^ xor_array`.  

This works because XOR cancels out the numbers present in the array.  

---

### Dry Run (Sum Method)  
Input: `[3,0,1]`  

- n = 3 → total sum = 3*(3+1)/2 = 6  
- sum of nums = 3+0+1 = 4  
- missing = 6 - 4 = 2 ✅  

Output: `2`  

---

## Resources for Learning  
- [LeetCode Problem 268: Missing Number](https://leetcode.com/problems/missing-number/)  
- [Sum Formula for Missing Number (GeeksforGeeks)](https://www.geeksforgeeks.org/find-the-missing-number/)  
- [XOR Trick for Missing Number Explained](https://www.geeksforgeeks.org/find-the-missing-number/)  

---
