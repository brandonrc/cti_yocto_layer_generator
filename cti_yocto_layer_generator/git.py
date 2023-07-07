from git import Repo
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clone_repo(repo_url, local_dir):
    try:
        Repo.clone_from(repo_url, local_dir)
        logger.info("Successfully cloned repo")
    except Exception as e:
        logger.error(f"Failed to clone repo: {str(e)}")

def check_branch_exists(repo, branch_name):
    existing_branches = repo.git.branch('-a').split()
    return branch_name in existing_branches

def create_branch(repo, branch_name):
    if not check_branch_exists(repo, branch_name):
        try:
            repo.git.checkout('-b', branch_name)
            logger.info("Successfully created and checked out new branch")
        except Exception as e:
            logger.error(f"Failed to create branch: {str(e)}")

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

def pull_changes(repo, branch_name='master'):
    try:
        origin = repo.remotes.origin
        origin.pull(branch_name)
        logger.info("Successfully pulled changes from remote branch")
    except Exception as e:
        logger.error(f"Failed to pull changes from remote branch: {str(e)}")

def push_changes(repo, branch_name='master'):
    try:
        origin = repo.remotes.origin
        origin.push(branch_name)
        logger.info("Successfully pushed changes to remote branch")
    except Exception as e:
        logger.error(f"Failed to push changes to remote branch: {str(e)}")

def sync_changes(repo_path, branch_name='master'):
    try:
        repo = Repo(repo_path)
        pull_changes(repo, branch_name)
        push_changes(repo, branch_name)
        logger.info("Successfully synchronized changes with remote branch")
    except Exception as e:
        logger.error(f"Failed to synchronize changes with remote branch: {str(e)}")
