import os.path
from git import *
import git, os, shutil

UPLOAD_FOLDER = "~/Desktop/gitpull/new"
if not os.path.exists(UPLOAD_FOLDER):
  os.makedirs(UPLOAD_FOLDER)
  print(UPLOAD_FOLDER)
new_path = os.path.join(UPLOAD_FOLDER)
DIR_NAME = new_path
REMOTE_URL = "https://github.com/google/capirca.git"   # Just a random url to test

class git_operation_clone():
  try:
    def __init__(self):
        self.DIR_NAME = DIR_NAME
        self.REMOTE_URL = REMOTE_URL

    def git_clone(self):

        if os.path.isdir(DIR_NAME):
            shutil.rmtree(DIR_NAME)
        os.mkdir(DIR_NAME)
        repo = git.Repo.init(DIR_NAME)
        origin = repo.create_remote('origin', REMOTE_URL)
        origin.fetch()
        origin.pull(origin.refs[0].remote_head)
  except Exception as e:
      print(str(e))

class conv_to_exe():
    def create():
        os.system("pyinstaller --onefile ~/Desktop/gitpull/samp.py")
class run_exe():
    def run():
        os.system("~/Desktop/gitpull/dist/samp.exe")

if __name__ == '__main__':
   git_operation_clone()
   git_operation_clone.git_clone('')  
   conv_to_exe.create()
   run_exe.run()

   
