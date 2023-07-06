import requests
import tarfile

def download_package(package_url, local_path):
    response = requests.get(package_url, stream=True)
    response.raise_for_status()

    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def extract_package(tar_path, extract_dir):
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=extract_dir)

# Add more functions as per your needs
