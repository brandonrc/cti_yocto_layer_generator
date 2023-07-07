"""
git.py

This module provides functionalities related to handling git operations. It includes functions to clone 
repositories, manage branches, commit changes, and push to remote.
"""

from git import Repo
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#
# Helper functions for git operations 


# Clone a repo
# Args:
# - repo_url: url of the repo to clone
# - local_dir: local directory to clone to
def clone_repo(repo_url, local_dir):
    try:
        Repo.clone_from(repo_url, local_dir)
        logger.info("Successfully cloned repo")
    except Exception as e:
        logger.error(f"Failed to clone repo: {str(e)}")

# Check if a branch exists in a repo
# Args:
# - repo_path: path to the repo
# - branch_name: name of the branch to check
# returns: True if the branch exists, False otherwise
def check_branch_exists(repo, branch_name):
    existing_branches = repo.git.branch('-a').split()
    return branch_name in existing_branches

# Create a new branch
# Args:
# - repo_path: path to the repo
#  - branch_name: name of the new branch
def create_branch(repo, branch_name):
    if not check_branch_exists(repo, branch_name):
        try:
            repo.git.checkout('-b', branch_name)
            logger.info("Successfully created and checked out new branch")
        except Exception as e:
            logger.error(f"Failed to create branch: {str(e)}")

# Checkout an existing branch
# Args:
# - repo_path: path to the repo
# - branch_name: name of the branch to checkout
def checkout_branch(repo_path, branch_name):
    try:
        repo = Repo(repo_path)
        if not check_branch_exists(repo, branch_name):
            create_branch(repo, branch_name)
        else:
            repo.git.checkout(branch_name)
            logger.info("Successfully checked out existing branch")
    except Exception as e:
        logger.error(f"Failed to checkout branch: {str(e)}")

# Pull changes from remote branch
# Args:
# - repo_path: path to the repo
# - branch_name: name of the branch to pull changes from
def pull_changes(repo, branch_name='master'):
    try:
        origin = repo.remotes.origin
        origin.pull(branch_name)
        logger.info("Successfully pulled changes from remote branch")
    except Exception as e:
        logger.error(f"Failed to pull changes from remote branch: {str(e)}")

# Push changes to remote branch
# Args:
# - repo_path: path to the repo
# - branch_name: name of the branch to push changes to 
def push_changes(repo, branch_name='master'):
    try:
        origin = repo.remotes.origin
        origin.push(branch_name)
        logger.info("Successfully pushed changes to remote branch")
    except Exception as e:
        logger.error(f"Failed to push changes to remote branch: {str(e)}")

# Sync changes with remote branch
# Args:
# - repo_path: path to the repo
# - branch_name: name of the branch to sync changes with
def sync_changes(repo_path, branch_name='master'):
    try:
        repo = Repo(repo_path)
        pull_changes(repo, branch_name)
        push_changes(repo, branch_name)
        logger.info("Successfully synchronized changes with remote branch")
    except Exception as e:
        logger.error(f"Failed to synchronize changes with remote branch: {str(e)}")

# Initialize a new repo
# Args:
# - repo_path: path to the new repo
def init_repo(repo_path):
    try:
        Repo.init(repo_path)
        logger.info("Successfully initialized new repo")
    except Exception as e:
        logger.error(f"Failed to initialize new repo: {str(e)}")