"""
package.py

This module provides functionalities related to handling the Connect Tech Inc's BSP packages. It includes
functions to download, extract, and process these packages.
"""

import requests
import tarfile

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
