"""
package.py

This module provides functionalities related to handling the Connect Tech Inc's BSP packages. It includes
functions to download, extract, and process these packages.
"""

import requests
import tarfile
import subprocess

# Add more functions as per your needs
# args:
#    package_url: URL of the package to download
#    local_path: Path to save the downloaded package to
def download_package(package_url, local_path):
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
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=extract_dir)

# Extracts all debian files in a debian package
# args:
#     deb_file_path: Path to the debian package
#     output_directory: Path to extract the debian files to
def extract_deb_files(deb_file_path, output_directory):
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