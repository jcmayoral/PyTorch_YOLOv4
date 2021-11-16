import sys

with open(sys.argv[2],'a') as nfile:
    with open(sys.argv[1],'r') as file:
        for line in file:
            tm = line.rstrip().split(" ")[0]
            print (tm)
            nfile.write(tm+"\n")

