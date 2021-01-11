import os
import shutil
import time
def main():
    file=input("Which file do you want to delete:")
    path=file
    def get_file_or_folder_age(path):
        days=30
        seconds=time.time()-(days*24*60*60)
        