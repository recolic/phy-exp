#!/bin/env python3
# -*- coding: UTF-8 -*-
# Gereric: Draw line.
# Recolic Keghart, Apr 29, 2017.

import numpy, sys
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from matplotlib import rcParams

arrX, arrY = [0, 4, 3, 2, 18, 5, 3, 5, 7, 3, 7], [0, 0.64, 0.55, 0.33, 2.92, 0.79, 0.50, 0.79, 1.14, 0.49, 1.15]
maxX, maxY = 20, 2
windowX, windowY = 12, 8


# Do calculate
# y = k x + b (I = k V + b)
print('Your input: ', arrX, '|', arrY)
print('Data collection done. Generating result...')
V, I = numpy.array(arrX), numpy.array(arrY)
def lineFunc(kb, v):
    k,b=kb
    return k*v + b

lossFunc = lambda kb, v, i : lineFunc(kb, v) - i

# Fire!
kb0 = [10,0]
kbFinal = leastsq(lossFunc, kb0, args=(V, I))
k,b=kbFinal[0]
print('Done. Y=', k, 'X +', b)

# Draw function map.
rcParams['grid.linestyle']='-'
rcParams['grid.color'] = 'blue'
rcParams['grid.linewidth'] = 0.2
plt.figure(figsize=(windowX, windowY))
plt.scatter(V,I,color="red",label="Sample Point",linewidth=3)
px=numpy.linspace(0,maxX,1000)
py=k*px+b
plt.plot(px,py,color="orange",label="Fitting Line",linewidth=2)
plt.legend()
plt.grid()
plt.show()

def toFloat(sstr):
    if sstr == '':
        return 0.0
    else:
        return float(sstr)
