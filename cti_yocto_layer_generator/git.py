from git import Repo

def clone_repo(repo_url, local_dir):
    Repo.clone_from(repo_url, local_dir)

def create_branch(repo_path, branch_name):
    repo = Repo(repo_path)
    repo.git.checkout('-b', branch_name)

# Add more functions as per your needs
