# GeoAI

GeoAI is a project that enables users to quickly download panoramas from given coordinates and sort them based on inference detections.

## Installation

To install GeoAI, follow these steps:

1. Clone the repository by running `git clone https://github.com/user/GeoAI.git`
2. Navigate to the directory containing the repository by running `cd GeoAI`
3. Run `python install.py` to install the necessary dependencies.

## Usage

1. Generate locations using the [map generator](https://map-generator.vercel.app/) and download them as a CSV file. This file will be referred to as your `locs` file.
2. Train your own weights for the object you want to detect. [Roboflow](https://blog.roboflow.com/yolov7-custom-dataset-training-tutorial/#training-a-custom-yolov7-model) has a well-written tutorial on how to do this.
3. Run `python geoai.py` with the following arguments:

```bash
usage: geoai.py [-h] [--weights WEIGHTS] [--locs LOCS] [--out OUT] [--conf CONF] [--detect DETECT] [--xpos XPOS]
[--ypos YPOS] [--zoom ZOOM] [--nbt NBT]

optional arguments:
-h, --help show this help message and exit
--weights WEIGHTS weights/example.pt
--locs LOCS csv file with locs in
--out OUT file to save as, eg data/out.csv
--conf CONF confidence threshold
--detect DETECT thing to detect (integer)
--xpos XPOS cbk x pos
--ypos YPOS cbk y pos
--zoom ZOOM cbk zoom
--nbt NBT cbk nbt
```

For example, if you want to run the program with the `locs` file `locations.csv`, the weights file `example.pt`, and save the output to `out.csv`, you would run the following command:
```py
python geoai.py --locs locations.csv --weights example.pt --out out.csv
```
If you have any questions, feel free to contact me on Discord at pig ✧.*#8774.
