import quickmap
import sys

with open(sys.argv[1]) as f:
    cont = f.read()

barr = []
for line in cont.split('\n'):
    if line == '':
        continue
    barr.append(float(line))

aarr = [i for i in range(len(barr))]
quickmap.GetMap(aarr, barr)
