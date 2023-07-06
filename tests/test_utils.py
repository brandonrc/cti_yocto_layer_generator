import os
from your_package.utils import create_directory, copy_file

def test_create_directory():
    create_directory("/tmp/test_dir")
    assert os.path.exists("/tmp/test_dir")

def test_copy_file():
    with open("/tmp/test_file", "w") as f:
        f.write("test")
    copy_file("/tmp/test_file", "/tmp/test_file_copy")
    assert os.path.exists("/tmp/test_file_copy")
