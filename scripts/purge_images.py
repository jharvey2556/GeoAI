import os
import glob

def main(img_path):
    files = glob.glob(img_path + "*")
    for f in files:
        os.remove(f)
    print("images deleted")