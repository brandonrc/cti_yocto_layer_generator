"""
utils.py

This module provides utility functions used across the project. It includes file handling operations, 
directory management functions, and other miscellaneous helper functions.
"""

import os
import shutil
import re


# Extract the Jetpack version from a filename.
# args:
# filename: the filename to extract the version from.
def extract_jetpack_version(filename):
    """Extract the Jetpack version from a filename."""
    # Split the filename on the '-' character
    parts = filename.split('-')

    # Iterate over the parts
    for part in parts:
        # Use a regular expression to check if the part is a version number
        match = re.match(r"\d+\.\d+\.\d+", part)
        if match:
            # If a match is found, return it
            return match.group()

    # If no match is found, return None
    return None


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
