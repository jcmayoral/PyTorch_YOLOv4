import sys
import os

new_file = open(sys.argv[1]+".filter", "a")

with open(sys.argv[1], 'r') as original:
    for line in original:
        label = line.strip().replace("png", "txt")
        if os.path.exists(label):
            new_file.write(line)
