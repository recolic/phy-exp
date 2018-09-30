import quickmap
import math, sys
with open(sys.argv[1]) as f:
    cont = f.read()

xrc = []
yrc = []
for line in cont.split('\n'):
    if line == '':
        continue
    x, y = line.split(' ')
    xrc.append(float(x)+2)
    yrc.append((float(y)))
    #yrc.append(math.log2(float(y)))

ylog = [(yrc[int(index/2)]+yrc[int((index+1)/2)])/2/ele for index, ele in enumerate(yrc)]
ylog = [math.log2(i) for i in ylog]
#ylog=yrc
quickmap.GetMap(xrc,ylog,smoothLine=False)
#quickmap.GetMap(xrc,ylog,polyLine=True,poly_inverseK=True,poly_maxXPower=10)
