import os
from PIL import Image

def main(img_path):
    directory = os.path.abspath(img_path)
    counter1 = 0
    counter2 = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            try:
                img = Image.open(f)
                counter1 += 1
            except:
                os.remove(f)
            counter2 += 1
