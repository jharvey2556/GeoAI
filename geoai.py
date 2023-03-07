from scripts.img_download import main as img_download
from scripts.checknum_save import main as checknum_save
from scripts.remove_corrupt import main as remove_corrupt
from scripts.purge_labels import main as purge_labels
from scripts.run_inference import main as run_inference
from scripts.write_results import main as write_results
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--weights', type=str, default="weights/best.pt", help='weights/example.pt')
parser.add_argument('--locs', type=str, default="data/locs.csv", help='csv file with locs in')
parser.add_argument('--out', type=str, default='data/out.csv', help='file to save as, eg data/out.csv')
parser.add_argument('--conf', type=int, default=0.7, help='confidence threshold')
parser.add_argument('--detect', type=str, default="0", help='thing to detect (integer)')
parser.add_argument('--xpos', type=int, default=0, help='cbk x pos')
parser.add_argument('--ypos', type=int, default=0, help='cbk y pos')
parser.add_argument('--zoom', type=int, default=0, help='cbk zoom')
parser.add_argument('--nbt', type=int, default=1, help='cbk nbt')
opt = parser.parse_args()

# key
key = "AIzaSyDqRTXlnHXELLKn7645Q1L_5oc4CswKZK4"

# paths
img_path = "images/"
detect_path = "yolov7/detect.py"
labels_path = "data/labels/"
checknum_path = "data/checknum.txt"

# settings
locs_path = opt.locs
weight_path = opt.weights
conf = opt.conf
detect_num = opt.detect
cbk_settings = [opt.xpos,opt.ypos,opt.zoom,opt.nbt]
out_path = opt.out

img_download(cbk_settings,locs_path,img_path,key)
remove_corrupt(img_path)
run_inference(detect_path,img_path,weight_path,conf,labels_path)
checknum_save(checknum_path,labels_path)
write_results(locs_path,labels_path,checknum_path,out_path,detect_num)
