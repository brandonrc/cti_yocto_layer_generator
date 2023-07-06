import os
import shutil

def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=True)

def copy_file(src_path, dst_path):
    shutil.copy(src_path, dst_path)

# Add more functions as per your needs
