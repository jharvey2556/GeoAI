import os
import csv

# locs_path,labels_path
def main(csvfile,directory,checknum_path,out_path,detect_num):
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    with open(checknum_path,"r") as f:
        rawdata = f.readlines()
        checknum_list = rawdata[0].split(",")

    with open(out_path, "w", encoding="UTF8", newline="") as csvf:
        writer = csv.writer(csvf)
        counter = 0
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                raw = filename[6:]
                raw = raw[:-4]
                if checknum_list[counter] == detect_num:
                    writer.writerow(rows[int(raw)])
                counter += 1
        print(f"locs saved in {out_path}")
