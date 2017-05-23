#!/bin/env python3
# -*- coding: UTF-8 -*-
# Hall effect: data processing. (This py will calc VH-Is and VH-Im)
# Recolic Keghart, Apr 29, 2017.

import numpy, sys
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from matplotlib import rcParams

Imax = 5 # Maybe you need to change it to 0.5 for Im
arrI, arrV = [], []

# Read data from file? File can include 'done' line or not. 
if len(sys.argv) == 2:
    fd = open(sys.argv[1])
    fcont = fd.read()
    fd.close()
    farr = fcont.split('\n')
    for s in farr:
        if s == 'done':
            break
        if s == '':
            print('Warning: empty data line ignored.')
            continue
        sarr = s.split(' ')
        if len(sarr) != 5:
            print('Warning: invalid data line ignored.')
            continue
        farr = [abs(float(v)) for v in sarr]
        arrI.append(farr[0])
        arrV.append(sum(farr[1:5]) / 4)
else: # Do data collect
    print('Give me your data please.')
    print('Format: Is(mA)/Im(A) V1(mV) V2 V3 V4')
    print('Example(It\'s ok to write 1.00 as 1):')
    print('>1.00 -1.50 1.43 -1.40 1.53')
    print('Input "done" to stop, and launch calculator.')
    print('Now, let\'s start! Be careful to your space.')
    while True:
        s = input('>')
        if s == 'done':
            break
        if s == '':
            print('Warning: empty data line ignored.')
            continue
        sarr = s.split(' ')
        if len(sarr) != 5:
            print('Warning: invalid data line ignored.')
            continue
        farr = [abs(float(v)) for v in sarr]
        arrI.append(farr[0])
        arrV.append(sum(farr[1:5]) / 4)

# Do calculate
# y = k x + b (V = k I + b)
print('Your input: ', arrI, '|', arrV)
print('Data collection done. Generating result...')
I, V = numpy.array(arrI), numpy.array(arrV)
def lineFunc(kb, i):
    k,b=kb
    return k*i+b

lossFunc = lambda kb, i, v : lineFunc(kb, i) - v

# Fire!
kb0 = [1,0]
kbFinal = leastsq(lossFunc, kb0, args=(I, V))
k,b=kbFinal[0]
print('Done. VH=', k, 'I* +', b)

# Draw function map.
rcParams['grid.linestyle']='-'
rcParams['grid.color'] = 'blue'
rcParams['grid.linewidth'] = 0.2
plt.figure(figsize=(8,6))
plt.scatter(I,V,color="red",label="Sample Point",linewidth=3)
px=numpy.linspace(0,Imax,1000)
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

# Calc more
print('Continue to get Hall constant.[If you\'re using VH-Im, press Ctrl-C to exit now]')
print('I need to know about your Hall element:')
d=toFloat(input('d(mm) 0.500 ?>'))
gsa=toFloat(input('B/Im(KGS/A) >'))
im=toFloat(input('Im(A) 0.450 ?>'))
if d == 0:
    d = 0.5
if gsa == 0:
    print('You MUST give gsa!')
    exit(1)
if im == 0:
    im = 0.45
hallC = k * d * 1e4 / (im * gsa) # KGs and mm
n = 1 / (hallC * 1.6021766208e-19)
print('RH(cm^3/C)(multiply 3pi/8 manually if you prefer)=', hallC, ', n(cm^-3)(divided 3pi/8 manually if you prefer)=', n)
print('Deal with statistical dispersion by yourself.')
