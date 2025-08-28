# 🔐 Hashing Algorithms in Python

## Overview

This folder contains implementations of hashing techniques commonly used in algorithm design and data structure problems. Hashing is a powerful method for efficiently storing and retrieving data, with applications in frequency counting, duplicate detection, and optimization problems. These implementations are essential for coding interviews and competitive programming.

## Quick Run Instructions

To run any of the Python files in this folder, use the following command:

```bash
python3 filename.py
```

For example, to run the frequency counting program:

```bash
python3 7_store_frequency_in_dictionary.py
```

Make sure you have Python 3 installed on your system. You can check by running:

```bash
python3 --version
```

## Problems/Algorithms

| File | Algorithm | Time Complexity | Space Complexity |
|------|-----------|----------------|------------------|
| [7_store_frequency_in_dictionary.py](7_store_frequency_in_dictionary.py) | Frequency counting using dictionary | O(n) | O(n) |
| [8_hashing.py](8_hashing.py) | Basic hashing concepts | Varies | Varies |

## Notes / Gotchas

- Python dictionaries are implemented as hash tables, making them very efficient for lookups (O(1) average case)
- When using the `get()` method with dictionaries, you can provide a default value which is returned if the key doesn't exist
- The `collections.Counter` class is a specialized dictionary for counting hashable objects
- Be careful with hash collisions in custom hash implementations (not typically an issue with Python's built-in dict)
- Hash tables provide excellent performance for problems involving frequency counting, membership testing, and deduplication

## Resources

- [GeeksforGeeks - Hashing Data Structure](https://www.geeksforgeeks.org/hashing-data-structure/)
- [Python Collections Module Documentation](https://docs.python.org/3/library/collections.html)
- [Wikipedia - Hash Table](https://en.wikipedia.org/wiki/Hash_table)
- [Real Python - Dictionaries in Python](https://realpython.com/python-dicts/)
