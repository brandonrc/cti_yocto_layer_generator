import os
import tempfile
from your_package.git import clone_repo, create_branch

def test_clone_repo():
    with tempfile.TemporaryDirectory() as tempdir:
        clone_repo("https://github.com/your_user/your_test_repo.git", tempdir)
        assert os.path.exists(os.path.join(tempdir, 'README.md'))  # assuming your test repo has a README.md file

def test_create_branch():
    with tempfile.TemporaryDirectory() as tempdir:
        clone_repo("https://github.com/your_user/your_test_repo.git", tempdir)
        create_branch(tempdir, "test_branch")
        # Check branch creation here. You might need to add a
