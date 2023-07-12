"""
generator.py

This is the main module of the CTI Yocto Layer Generator. It uses functionalities from the git, package, 
and utils modules to convert Connect Tech Inc's BSP layers into Yocto layers.
"""
import os
import uuid
import shutil
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from . import git_helpers
from . import package
from . import utils
from . import yocto_helpers

class CTILayerGenerator:
    def __init__(self, repo_url, package_url, offline_mode, yocto_version):
        self.repo_url = repo_url
        self.package_url = package_url
        self.offline_mode = offline_mode
        self.yocto_version = yocto_version
        self.filename = os.path.basename(package_url)
        self.jetpack_version = utils.extract_jetpack_version(self.filename)
        self.branch_name = f"{yocto_version}-l4t-r{self.jetpack_version}"
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
        logger.info("Starting to generate layers...")
        
        self.setup_directories()

        if self.offline_mode:
            git_helpers.init_repo(self.repo_dir)
        else:
            git_helpers.clone_repo(self.repo_url, self.repo_dir)
        
        git_helpers.create_branch(self.repo_dir, self.branch_name)
        git_helpers.checkout_branch(self.repo_dir, self.branch_name)
            
        package_path = os.path.join(self.package_dir, os.path.basename(self.package_url))
        extracted_path = os.path.join(self.extracted_dir, os.path.splitext(os.path.basename(self.package_url))[0])

        if not os.path.exists(package_path):
            logger.info(f"Package does not exist at {package_path}, downloading it...")
            package.download_package(self.package_url, package_path)
            
        if not os.path.exists(extracted_path):
            logger.info(f"Package has not been extracted at {extracted_path}, extracting it...")
            package.extract_package(package_path, extracted_path)
            
        yocto_helpers.create_layer_skeleton(self.repo_dir)
        yocto_helpers.create_basic_config_files(self.repo_dir, utils.get_machine_name_from_package(os.path.basename(self.package_url)), self.yocto_version)
            
        # Search for all debs in extracted_packages directory then 
        # extract them into the debs directory
        for root, dirs, files in os.walk(extracted_path):
            for file in files:
                if file.endswith(".deb"):
                    package_name = file.rsplit('.', 1)[0]  # cut off the .deb
                    tmp_package_dir = os.path.join(self.debs_dir, package_name)
                    # print("Extracting deb file:")
                    # print(tmp_package_dir)
                    os.makedirs(tmp_package_dir, exist_ok=True)  # Ensure directory is created if it doesn't already exist
                    deb_file_path = os.path.join(root, file)
                    logger.info(f"Extracting deb files from {deb_file_path} to {self.repo_dir}")
                    # package.extract_deb_files(deb_file_path, tmp_package_dir)
                    package.extract_deb_files_and_create_bb(deb_file_path, self.repo_dir)
        

        # here you'd continue with your generation logic, using self.repo_dir and extracted_path as the paths

        # and then clean up the directories if you want
        # Not sure if we want to delete the directories or
        # if we want to keep them for the next run
        # self.cleanup_directories()