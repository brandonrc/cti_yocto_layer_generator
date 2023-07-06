import os
import tempfile
from your_package.package import download_package, extract_package

def test_download_package():
    with tempfile.TemporaryDirectory() as tempdir:
        download_package("https://example.com/test_package.tgz", os.path.join(tempdir, "test_package.tgz"))
        assert os.path.exists(os.path.join(tempdir, "test_package.tgz"))

def test_extract_package():
    with tempfile.TemporaryDirectory() as tempdir:
        download_package("https://example.com/test_package.tgz", os.path.join(tempdir, "test_package.tgz"))
        extract_package(os.path.join(tempdir, "test_package.tgz"), tempdir)
        # assert existence of a file or directory here that should exist after extracting the package
