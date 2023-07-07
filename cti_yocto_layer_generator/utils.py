"""
utils.py

This module provides utility functions used across the project. It includes file handling operations, 
directory management functions, and other miscellaneous helper functions.
"""

import os
import shutil

# Create a directory if it doesn't exist.
# args:
#  dir_path: the path to the directory to create.
def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=True)

# Copy a file from one location to another.
# args:
# src_path: the path to the source file.
# dst_path: the path to the destination file.
def copy_file(src_path, dst_path):
    shutil.copy(src_path, dst_path)
