# Import statements
import os
import datetime
from git import Repo

# Class that has all the functionality needed for "was it Rufus"
class GitInfoRufus:
    def __init__(self, git_dir):
        self.git_dir = git_dir
        self.repo = Repo(git_dir)
        self.git = self.repo.git

    def repo_info(self):
        # Get the head commit object
        head_commit = self.repo.head.commit
        # Get the committed datetime object of the head commit and remove microseconds
        commit_date = head_commit.committed_datetime.replace(microsecond=0)
        # Get the current datetime object in UTC and subtract one week
        week_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)
        # convert commit_date to UTC
        commit_date = commit_date.astimezone(datetime.timezone.utc)
        
        # Print the name of the active branch
        print(f"Active branch: {self.repo.active_branch.name}")
        # Check if there are any modified files
        print(f"Modified files: {'working tree clean' not in self.git.status()}")
        # Check if the commit is recent commit
        print(f"Recent commit: {commit_date > week_ago}")
        # Check if the commit is recent commit was authored by 
        print(f"Commit by Rufus: {head_commit.author.name == 'Rufus'}")

# Main for debugging purpose
if __name__ == "__main__":
    # Print the working directory 
    print(os.getcwd())
    # Input the working directory for the user
    git_dir = input("Input directory in which to assess git status: ")
    # Make an object to call the function
    git_info = GitInfoRufus(git_dir)
    # Calling the function repo_info to see the results
    git_info.repo_info()
