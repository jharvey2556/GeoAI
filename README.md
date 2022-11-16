# GeoAI

GeoAI is a project made for quickly downloading panoramas from co-ordinates and sorting based on inference detections

## Installation

Clone repo and run install.py

## Usage

Generate locations with https://map-generator.vercel.app/ and download as csv, this will be your locs file

You will need to train your own weights for the thing you are trying to detect
Roboflow has a well written blog of how to start
https://blog.roboflow.com/yolov7-custom-dataset-training-tutorial/#training-a-custom-yolov7-model

Any questions please feel free to contact me on discord at `pig ✧.*#8774`

```bash
python geoai.py -h
usage: geoai.py [-h] [--weights WEIGHTS] [--locs LOCS] [--out OUT] [--conf CONF] [--detect DETECT] [--xpos XPOS]
                [--ypos YPOS] [--zoom ZOOM] [--nbt NBT]

optional arguments:
  -h, --help         show this help message and exit
  --weights WEIGHTS  weights/example.pt
  --locs LOCS        csv file with locs in
  --out OUT          file to save as, eg data/out.csv
  --conf CONF        confidence threshold
  --detect DETECT    thing to detect (integer)
  --xpos XPOS        cbk x pos
  --ypos YPOS        cbk y pos
  --zoom ZOOM        cbk zoom
  --nbt NBT          cbk nbt
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
