import os

def main(checknum_path,labels_path):
    directory = os.path.abspath(labels_path)
    checklist = []

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            with open(f, "r") as rf:
                num = rf.read(1)
                checklist.append(num)

    with open(checknum_path,"w") as f:
        for entry in checklist:
            f.write(entry +  ",")

    print("finished checknum save")

