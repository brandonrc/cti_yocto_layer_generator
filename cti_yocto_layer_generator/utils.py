"""
utils.py

This module provides utility functions used across the project. It includes file handling operations, 
directory management functions, and other miscellaneous helper functions.
"""

import os
import shutil
import re
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Extract the Jetpack version from a filename.
# args:
# filename: the filename to extract the version from.
def extract_jetpack_version(filename):
    logger.info(f"Extracting Jetpack version from {filename}")
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
    logger.info(f"Creating directory at {dir_path}")
    os.makedirs(dir_path, exist_ok=True)

# Copy a file from one location to another.
# args:
# src_path: the path to the source file.
# dst_path: the path to the destination file.
def copy_file(src_path, dst_path):
    logger.info(f"Copying file from {src_path} to {dst_path}")
    shutil.copy(src_path, dst_path)


# Get the machine name from a package name.
# args:
# package_name: the name of the package.
def get_machine_name_from_package(package_name):
    # Regular expression to find the part of the name to remove
    pattern = "-[0-9]+\.[0-9]+\.[0-9]+.*"

    # Search for the pattern in the package name
    result = re.search(pattern, package_name)

    # Check if the pattern was found
    if result is None:
        logger.error(f"No version number found in package name: {package_name}")
        return None

    # Strip off the version number and anything after it, and convert to lowercase
    machine_name = package_name[:result.start()].lower()

    return machine_name

def get_tegra_soc(machine_name):
    if "orin" in machine_name:
        return "tegra234"
    elif "xavier" in machine_name:
        return "tegra194"
    elif "tx2" in machine_name:
        return "tegra186"
    elif "tx1" in machine_name or "nano" in machine_name:
        return "tegra210"
    else:
        logger.error(f"Unknown Tegra SoC for machine name: {machine_name}")
        return None