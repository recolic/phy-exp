#!/bin/env python3
# -*- coding: UTF-8 -*-
# Gereric: Draw line.
# Recolic Keghart, Apr 29, 2017.

import numpy
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from matplotlib import rcParams

def dotMultiply(vctA, vctB):
    if len(vctA) != len(vctB):
        print("Error: While vcta is ", vctA, " and vctb is ", vctB)
        raise ValueError("dotmulti needs lena == lenb.")
    ans = 0
    for a, b in zip(vctA, vctB):
        ans += a * b
    return ans

def GetMap(parrX, parrY, windowSizeX=12, windowSizeY=8, extendXRate=1, extendYRate=1, line=False, passO=False, maxXPower=1, inverseK=False):
    print('Generic-GetMap by Recolic.')
    arrX, arrY = parrX, parrY
    maxX, maxY = max(arrX) * extendXRate, max(arrY) * extendYRate
    minX, minY = min(arrX) * extendXRate, min(arrY) * extendYRate
    # Do calculate
    # y = [k0 k1 k2 ...] dot [x^0 x^1 x^2 ...]
    print('Your input: ', arrX, '|', arrY)
    print('Data collection done. Generating result...')
    X, Y = numpy.array(arrX), numpy.array(arrY)

    def lineFunc(k, x):
        vctX = [x ** power for power in range(maxXPower + 1)]
        if passO:
            vctX[0] = 0
        return dotMultiply(k, vctX)

    def lossFunc(k, x, y): return abs(lineFunc(k, x) - y)

    # Fire!
    if line:
        kInit = [1 for _ in range(maxXPower + 1)]
        kInit[0] = 0 # guarantee passO.
        if inverseK:
            kFinal, _ = leastsq(lossFunc, kInit, args=(Y, X))
            print('Fit line done. k^-1=', kFinal)
        else:
            kFinal, _ = leastsq(lossFunc, kInit, args=(X, Y))
            print('Fit line done. k=', kFinal)
    else:
        print('Drawing map without fitting a line...')

    # Draw function map.
    rcParams['grid.linestyle'] = '-'
    rcParams['grid.color'] = 'blue'
    rcParams['grid.linewidth'] = 0.2
    plt.figure(figsize=(windowSizeX, windowSizeY))
    plt.scatter(X, Y, color="red", label="Sample Point", linewidth=3)
    if line:
        if inverseK:
            py = numpy.linspace(minY, maxY, 1000)
            px = dotMultiply(kFinal, [py ** power for power in range(maxXPower + 1)])
        else:
            px = numpy.linspace(minX, maxX, 1000)
            py = dotMultiply(kFinal, [px ** power for power in range(maxXPower + 1)])
        plt.plot(px, py, color="orange", label="Fitting Line", linewidth=2)
    plt.legend()
    plt.grid()
    plt.show()

    def toFloat(sstr):
        if sstr == '':
            return 0.0
        else:
            return float(sstr)
