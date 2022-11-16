from scripts.purge_labels import main as purge_labels
import os

def main(detect_path,img_path,weight_path,conf,labels_path):
    response = input("run inference Y/N ")
    if response == "Y":
        purge_labels(labels_path)
        os.system(f"python {detect_path} --source {img_path} --weights {weight_path} --conf {conf} --save-txt --nosave --img-size 512 --project ./ --name data --no-trace --exist-ok")
