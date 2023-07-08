"""
package.py

This module provides functionalities related to handling the Connect Tech Inc's BSP packages. It includes
functions to download, extract, and process these packages.
"""

import requests
import tarfile
import subprocess
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add more functions as per your needs
# args:
#    package_url: URL of the package to download
#    local_path: Path to save the downloaded package to
def download_package(package_url, local_path):
    logger.info(f"Downloading package from {package_url} to {local_path}")
    response = requests.get(package_url, stream=True)
    response.raise_for_status()

    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

# Add more functions as per your needs
# args:
#     tar_path: Path to the tar file to extract
#     extract_dir: Path to extract the tar file to
def extract_package(tar_path, extract_dir):
    logger.info(f"Extracting package from {tar_path} to {extract_dir}")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=extract_dir)

# Extracts all debian files in a debian package
# args:
#     deb_file_path: Path to the debian package
#     output_directory: Path to extract the debian files to
def extract_deb_files(deb_file_path, output_directory):
    logger.info(f"Extracting deb files from {deb_file_path} to {output_directory}")
    command = ["dpkg", "-x", deb_file_path, output_directory]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # print("Extraction successful")
        # print("stdout:", result.stdout)
        # print("stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Extraction failed")
        print("Error:", e)
        print("stdout:", e.stdout)
        print("stderr:", e.stderr)
        
        
def create_bb_files(debs_dir):
    logger.info(f"Creating .bb files in {debs_dir}")
    for deb in os.listdir(debs_dir):
        # Get the path of the extracted deb directory
        deb_path = os.path.join(debs_dir, deb)
        # Skip if it's not a directory
        if not os.path.isdir(deb_path):
            continue

        # Create a directory for the bb file
        bb_dir_path = os.path.join(debs_dir, deb)
        os.makedirs(bb_dir_path, exist_ok=True)

        # Create the .bb file
        bb_file_path = os.path.join(bb_dir_path, f"{deb}.bb")
        with open(bb_file_path, 'w') as f:
            f.write(f"# {deb} BitBake recipe\n")

        logger.info(f"Created .bb file at {bb_file_path}")
        
        
def extract_deb_files_and_create_bb(deb_file_path, yocto_dir):
    logger.info(f"Extracting deb files from {deb_file_path} to {yocto_dir}")

    # Get the name of the debian package without the file extension
    deb_name = os.path.basename(deb_file_path).replace('.deb', '')

    # Determine the recipe directory based on the type of debian package
    if 'utils' in deb_name:
        recipes_dir = 'recipes-utils'
    elif 'config' in deb_name:
        recipes_dir = 'recipes-config'
    elif 'kernel' in deb_name:
        recipes_dir = 'recipes-kernel'
    elif 'dtbs' in deb_name:
        recipes_dir = 'recipes-dtbs'
    elif 'headers' in deb_name:
        recipes_dir = 'recipes-headers'
    else:
        recipes_dir = 'recipes-unknown'

    # Construct the full paths for the recipe and files directories
    recipe_dir_path = os.path.join(yocto_dir, recipes_dir, deb_name)
    files_dir_path = os.path.join(recipe_dir_path, 'files')

    # Create the recipe and files directories
    os.makedirs(files_dir_path, exist_ok=True)

    # Extract the debian package to the files directory
    command = ["dpkg", "-x", deb_file_path, files_dir_path]
    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
        logger.info(f"Extracted deb files to {files_dir_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to extract deb files: {e}")
        return

    # Create the .bb file in the recipe directory
    bb_file_path = os.path.join(recipe_dir_path, f"{deb_name}.bb")
    with open(bb_file_path, 'w') as f:
        f.write(f"# {deb_name} BitBake recipe\n")

    logger.info(f"Created .bb file at {bb_file_path}")


