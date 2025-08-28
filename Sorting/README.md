# 🔄 Sorting Algorithms in Python

## Overview

This folder contains implementations of classic sorting algorithms that are fundamental to computer science. Sorting is one of the most common operations in programming and is frequently tested in coding interviews. Understanding the trade-offs between different sorting algorithms in terms of time complexity, space complexity, and stability is essential for any developer.

## Quick Run Instructions

To run any of the Python files in this folder, use the following command:

```bash
python3 filename.py
```

For example, to run the merge sort implementation:

```bash
python3 mergesort.py
```

Make sure you have Python 3 installed on your system. You can check by running:

```bash
python3 --version
```

## Problems/Algorithms

| File | Algorithm | Time Complexity | Space Complexity | Stable |
|------|-----------|----------------|------------------|--------|
| [bubble_sort.py](bubble_sort.py) | Bubble Sort | O(n²) | O(1) | Yes |
| [Insertion_sort.py](Insertion_sort.py) | Insertion Sort | O(n²) | O(1) | Yes |
| [mergesort.py](mergesort.py) | Merge Sort | O(n log n) | O(n) | Yes |
| [selection_sort.py](selection_sort.py) | Selection Sort | O(n²) | O(1) | No |

## Notes / Gotchas

- Bubble sort has a best-case time complexity of O(n) when optimized with an early termination condition
- Merge sort is stable and has consistent O(n log n) performance, making it reliable for large datasets
- Quick sort (not implemented here but commonly used) has an average time complexity of O(n log n) but worst-case O(n²)
- Selection sort minimizes the number of swaps but is not stable
- Insertion sort is efficient for small datasets and is adaptive (performs better on partially sorted data)
- Python's built-in `sorted()` function uses Timsort, which is a hybrid stable sorting algorithm

## Resources

- [GeeksforGeeks - Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)
- [Visualizing Sorting Algorithms](https://www.toptal.com/developers/sorting-algorithms)
- [Big-O Cheat Sheet for Sorting Algorithms](https://www.bigocheatsheet.com/)
- [Python Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
