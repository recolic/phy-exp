#!/bin/env python3
# -*- coding: UTF-8 -*-
# Gereric: Draw line.
# Recolic Keghart, Apr 29, 2017.

import numpy
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from matplotlib import rcParams

def GetMap(parrX, parrY, windowX = 12, windowY = 8, line = False, passO = False):
    print('Generic-GetMap by Recolic.')
    arrX, arrY = parrX, parrY
    maxX, maxY = max(arrX)*1.2, max(arrY)*1.25

    # Do calculate
    # y = k x + b (I = k V + b)
    print('Your input: ', arrX, '|', arrY)
    print('Data collection done. Generating result...')
    V, I = numpy.array(arrX), numpy.array(arrY)
    def lineFunc(kb, v):
        k,b=kb
        if passO:
            return k*v
        else:
            return k*v+b

    lossFunc = lambda kb, v, i : lineFunc(kb, v) - i

    # Fire!
    if line:
        kb0 = [10,0]
        kbFinal = leastsq(lossFunc, kb0, args=(V, I))
        k,b=kbFinal[0]
        print('Fit line done. Y=', k, 'X +', b)
    else:
        print('Drawing map without fitting a line...')

    # Draw function map.
    rcParams['grid.linestyle']='-'
    rcParams['grid.color'] = 'blue'
    rcParams['grid.linewidth'] = 0.2
    plt.figure(figsize=(windowX, windowY))
    plt.scatter(V,I,color="red",label="Sample Point",linewidth=3)
    if line:
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