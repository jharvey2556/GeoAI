import os
import glob

def main(labels_path):
    response = input("purge labels folder Y/N ")
    if response == "Y":
        files = glob.glob(labels_path + "*")
        for f in files:
            os.remove(f)
        