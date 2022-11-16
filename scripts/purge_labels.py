import os
import glob

def main(labels_path):
       files = glob.glob(labels_path + "*")
       for f in files:
           os.remove(f)
        
