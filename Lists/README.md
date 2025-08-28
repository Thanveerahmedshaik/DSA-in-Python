# 📋 Array and List Algorithms in Python

## Overview

This folder contains algorithms and problems related to arrays and lists, which are fundamental data structures in programming. These implementations cover common operations like searching, sorting, rotating, and manipulating arrays. Array problems are frequently asked in coding interviews and form the foundation for more complex data structures.

## Quick Run Instructions

To run any of the Python files in this folder, use the following command:

```bash
python3 filename.py
```

For example, to find the largest element in an array:

```bash
python3 largest_element_in_array.py
```

Make sure you have Python 3 installed on your system. You can check by running:

```bash
python3 --version
```

## Problems/Algorithms

| File | Algorithm | Time Complexity | Space Complexity |
|------|-----------|----------------|------------------|
| [Find_mising_number_in_Array.py](Find_mising_number_in_Array.py) | Find missing number in array | O(n) | O(1) |
| [if_array_sorted.py](if_array_sorted.py) | Check if array is sorted | O(n) | O(1) |
| [largest_element_in_array.py](largest_element_in_array.py) | Find largest element in array | O(n) | O(1) |
| [Linear_search.py](Linear_search.py) | Linear search in array | O(n) | O(1) |
| [merge_two_sorted_arrays_without_duplicates.py](merge_two_sorted_arrays_without_duplicates.py) | Merge two sorted arrays | O(m+n) | O(m+n) |
| [remove_duplicates_in_a_sorted_array.py](remove_duplicates_in_a_sorted_array.py) | Remove duplicates from sorted array | O(n) | O(1) |
| [right_rotate_array_by_1_place.py](right_rotate_array_by_1_place.py) | Right rotate array by 1 position | O(n) | O(1) |
| [second_largest_element_in_array.py](second_largest_element_in_array.py) | Find second largest element | O(n) | O(1) |

## Notes / Gotchas

- Array indices in Python start from 0, which can be a source of off-by-one errors
- When rotating arrays, consider both left and right rotation approaches
- For problems involving sorted arrays, consider using binary search for O(log n) time complexity
- Be careful with edge cases like empty arrays, single element arrays, and duplicate elements
- In-place operations save space but can be trickier to implement correctly
- Two-pointer techniques are often useful for array problems
- Python lists are dynamic arrays with O(1) access time but O(n) insertion/deletion in the worst case

## Resources

- [GeeksforGeeks - Arrays Data Structure](https://www.geeksforgeeks.org/array-data-structure/)
- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Array Interview Questions](https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/)
- [Two Pointer Technique](https://www.geeksforgeeks.org/two-pointers-technique/)
