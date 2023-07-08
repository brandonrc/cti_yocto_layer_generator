"""
generator.py

This is the main module of the CTI Yocto Layer Generator. It uses functionalities from the git, package, 
and utils modules to convert Connect Tech Inc's BSP layers into Yocto layers.
"""
import os
import uuid
import shutil

from . import git
from . import package
from . import utils

class CTILayerGenerator:
    def __init__(self, repo_url, package_url, offline_mode, yocto_version):
        self.repo_url = repo_url
        self.package_url = package_url
        self.offline_mode = offline_mode
        self.yocto_version = yocto_version
        self.filename = os.path.basename(package_url)
        self.jetpack_version = utils.get_jetpack_version(self.filename)
        branch_name = f"{yocto_version}-l4t-r{self.jetpack_version}"
        self.uuid = str(uuid.uuid4())
        self.base_dir = os.path.expanduser("~/.cache/cti_yocto_layer_generator/")
        self.run_dir = os.path.join(self.base_dir, self.uuid)
        self.package_dir = os.path.join(self.run_dir, "packages")
        self.extracted_dir = os.path.join(self.run_dir, "extractedpackages")
        self.repo_dir = os.path.join(self.run_dir, "repo")
        self.debs_dir = os.path.join(self.run_dir, "debs")

    # setup the directories
    # Creates package, extracted, and repo directories
    def setup_directories(self):
        # create the necessary directories
        os.makedirs(self.package_dir, exist_ok=True)
        os.makedirs(self.extracted_dir, exist_ok=True)
        os.makedirs(self.repo_dir, exist_ok=True)
        os.makedirs(self.debs_dir, exist_ok=True)

    # clean up the directories
    # Delete the directories
    def cleanup_directories(self):
        # delete the directories
        shutil.rmtree(self.run_dir)

    # This is the main class of the CTI Yocto Layer Generator. 
    # It uses functionalities from
    def generate(self):
        self.setup_directories()

        if self.offline_mode:
            git.init_repo(self.repo_dir)
        else:
            git.clone_repo(self.repo_url, self.repo_dir)
            
        package_path = os.path.join(self.package_dir, os.path.basename(self.package_url))
        extracted_path = os.path.join(self.extracted_dir, os.path.splitext(os.path.basename(self.package_url))[0])

        if not os.path.exists(package_path):
            package.download_package(self.package_url, package_path)
            
        if not os.path.exists(extracted_path):
            package.extract_package(package_path, extracted_path)
            
        # Search for all debs in extracted_packages directory then 
        # extract them into the debs directory
        for root, dirs, files in os.walk(extracted_path):
            for file in files:
                if file.endswith(".deb"):
                    package_name = file.rsplit('.', 1)[0]  # cut off the .deb
                    # tmp_package_dir = os.path.join(self.debs_dir, package_name)
                    # print("Extracting deb file:")
                    # print(tmp_package_dir)
                    # os.makedirs(tmp_package_dir, exist_ok=True)  # Ensure directory is created if it doesn't already exist
                    deb_file_path = os.path.join(root, file)
                    package.extract_deb_files(deb_file_path, self.debs_dir)
        

        # here you'd continue with your generation logic, using self.repo_dir and extracted_path as the paths

        # and then clean up the directories if you want
        # Not sure if we want to delete the directories or
        # if we want to keep them for the next run
        # self.cleanup_directories()