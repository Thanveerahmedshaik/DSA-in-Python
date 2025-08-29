# conftest.py — make the repository root importable during pytest runs
import os
import sys

# Absolute path to the repo root (the directory this file lives in)
REPO_ROOT = os.path.abspath(os.path.dirname(__file__))

# Put repo root at the **front** of sys.path so `from Leetcode...` works
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
