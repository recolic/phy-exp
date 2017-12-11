#!/bin/env python3
# -*- coding: UTF-8 -*-
# Gereric: Draw line.
# Recolic Keghart, Apr 29, 2017.

import numpy
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.interpolate import spline

def dotMultiply(vctA, vctB):
    if len(vctA) != len(vctB):
        print("Error: While vcta is ", vctA, " and vctb is ", vctB)
        raise ValueError("dotmulti needs lena == lenb.")
    ans = 0
    for a, b in zip(vctA, vctB):
        ans += a * b
    return ans

def GetMap(arrX, arrY, windowSizeX=12, windowSizeY=8, extendXRate=1, extendYRate=1, polyLine=False, poly_passO=False, poly_maxXPower=1, poly_inverseK=False, smoothLine=False):
    '''
    Arguments:
    arrX and arrY: array of coordinates of points. Ex: GetMap([1,2,3,4,5], [1,2,3,4,5]) -> y=x
    polyLine(conflict with polyLine): Should I draw a fitting line by polynomial fitting?
    smoothLine(conflict with smoothLine): Should I draw a fitting line by connecting all points and smooth them?
    passO: Should the fitting line pass (0,0)? That's saying, should k0 be zero?
    maxXPower: If I should draw a fitting line, what polynomial function should I use? Ex: GetMap([1,2,3,4,5], [1,4,9,16,25], line=True, maxXPower) -> y=x^2
    inverseK: Usually, I'm drawing the curl `y=KX`, while K=[k0,k1,k2,...], X=[x^0,x^1,x^2,...]. If this switch is set, I'll drawing the curl `KY=x`. Don't worry, this switch is transparent to you.
    Ex: GetMap([0,1,1,4,4,9,9], [0,1,-1,2,-2,3,-3], poly_maxXPower=2, polyLine=True, poly_inverseK=True) -> y^2=x
    
    ReturnValue:
    void
    '''
    if polyLine and smoothLine:
        raise RuntimeError("bad argument: polyLine and smoothLine can't been set simultaneously.")
    if len(arrX) != len(arrY):
        raise ValueError("arrX and arrY must in same size, but {} != {}.".format(len(arrX), len(arrY)))
    print('Generic-GetMap by Recolic.')
    maxX, maxY = max(arrX) * extendXRate, max(arrY) * extendYRate
    minX, minY = min(arrX) * extendXRate, min(arrY) * extendYRate
    X, Y = numpy.array(arrX), numpy.array(arrY)
    print('Your input: ', arrX, '|', arrY)
    if polyLine:
        print('You want a polynomial fitting, with maxXPower = {}, passO = {}, inverseK = {}.'.format(poly_maxXPower, poly_passO, poly_inverseK))
    if smoothLine:
        print('You want a smooth fitting.')
    print('Generating result...')

    # y = [k0 k1 k2 ...] dot [x^0 x^1 x^2 ...]
    def lineFunc(k, x):
        vctX = [x ** power for power in range(poly_maxXPower + 1)]
        if poly_passO:
            vctX[0] = 0
        return dotMultiply(k, vctX)

    def lossFunc(k, x, y): return abs(lineFunc(k, x) - y)

    # Fire!
    if polyLine:
        kInit = [1 for _ in range(poly_maxXPower + 1)]
        kInit[0] = 0 # guarantee passO.
        if poly_inverseK:
            kFinal, _ = leastsq(lossFunc, kInit, args=(Y, X))
            print('Fitting line done. k^-1=', kFinal)
        else:
            kFinal, _ = leastsq(lossFunc, kInit, args=(X, Y))
            print('Fitting line done. k=', kFinal)
    else:
        print('Drawing map without fitting a line...')

    # Draw function map.
    rcParams['grid.linestyle'] = '-'
    rcParams['grid.color'] = 'blue'
    rcParams['grid.linewidth'] = 0.2
    plt.figure(figsize=(windowSizeX, windowSizeY))
    plt.scatter(X, Y, color="red", label="Sample Point", linewidth=3)
    if polyLine:
        if poly_inverseK:
            py = numpy.linspace(minY, maxY, 1000)
            px = dotMultiply(kFinal, [py ** power for power in range(poly_maxXPower + 1)])
        else:
            px = numpy.linspace(minX, maxX, 1000)
            py = dotMultiply(kFinal, [px ** power for power in range(poly_maxXPower + 1)])
        plt.plot(px, py, color="orange", label="Fitting Line", linewidth=2)
    if smoothLine:
        px = numpy.linspace(minX, maxX, 1000)
        py = spline(X, Y, px)
        plt.plot(px, py, color="orange", label="Fitting Line", linewidth=2)
    plt.legend()
    plt.grid()
    plt.show()

    def toFloat(sstr):
        if sstr == '':
            return 0.0
        else:
            return float(sstr)

def _str_remove_extra_space(s):
    begin, end = 0, len(s)
    for char in s:
        if char == ' ':
            begin += 1
        else:
            break
    for char in s[::-1]:
        if char == ' ':
            end -= 1
        else:
            break
    return s[begin:end]

def _str_remove_comments(s, commentSym = '#'):
    pos = s.find(commentSym)
    if pos == -1:
        return s
    else:
        return s[0:pos]

def DataFileToXYArray(fname, lineDelimiter = '\n', wordDelimiter = ' ', commentSym = '#', _DataType = float):
    '''
    give file name, return tuple: ([_DataType], [_DataType])
                                       (xArray, yArray)
    Default _DataType is python float, and I think that's enough.

    Example:
    x, y = DataFileToXYArray('test.dat')
    GenMap(x, y)
    '''
    with open(fname, 'r') as fd:
        s = fd.read()
    xArray, yArray = [], []
    for ori_line in s.split(lineDelimiter):
        line = _str_remove_comments(ori_line, commentSym)
        line = _str_remove_extra_space(line)
        if len(line) == '':
            continue
        ar = line.split(wordDelimiter)
        if len(ar) < 2:
            print('Warning: Bad data line "{}" skipped.'.format(ori_line))
            continue
        if len(ar) > 2:
            print('Warning: Invalid data line "{}" parsed as "{} {}"'.format(ori_line, ar[0], ar[1]))
        try:
            xArray.append(_DataType(ar[0]))
            yArray.append(_DataType(ar[1]))
        except:
            print('At data line "{}":'.format(ori_line))
    return xArray, yArray
        