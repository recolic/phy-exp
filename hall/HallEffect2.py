#!/bin/env python3
# -*- coding: UTF-8 -*-
# Hall effect: data processing. (This py will calc Is-V6)
# Recolic Keghart, Apr 29, 2017.

import numpy, sys
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from matplotlib import rcParams

arrV, arrI = [], []

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
        if len(sarr) != 2:
            print('Warning: invalid data line ignored.')
            continue
        farr = [abs(float(v)) for v in sarr]
        arrV.append(farr[1])
        arrI.append(farr[0])
else: # Do data collect
    print('Give me your data please.')
    print('Format: Is(mA) V6(mV)')
    print('Example(It\'s ok to write 1.00 as 1):')
    print('>0.10 -8.5')
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
        if len(sarr) != 2:
            print('Warning: invalid data line ignored.')
            continue
        farr = [abs(float(v)) for v in sarr]
        arrV.append(farr[1])
        arrI.append(farr[0])

# Do calculate
# y = k x + b (I = k V + b)
print('Your input: ', arrV, '|', arrI)
print('Data collection done. Generating result...')
V, I = numpy.array(arrV), numpy.array(arrI)
def lineFunc(kb, v):
    k,b=kb
    return k*v+b

lossFunc = lambda kb, v, i : lineFunc(kb, v) - i

# Fire!
kb0 = [10,0]
kbFinal = leastsq(lossFunc, kb0, args=(V, I))
k,b=kbFinal[0]
print('Done. Is=', k, 'V6 +', b)

# Draw function map.
rcParams['grid.linestyle']='-'
rcParams['grid.color'] = 'blue'
rcParams['grid.linewidth'] = 0.2
plt.figure(figsize=(1,10))
plt.scatter(V,I,color="red",label="Sample Point",linewidth=3)
px=numpy.linspace(0,100,1000)
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
print('Continue to get electric conductivity.')
print('I need to know about your Hall element:')
d=toFloat(input('d(mm) 0.500 ?>'))
b=toFloat(input('b(mm) 4.00 ?>'))
l=toFloat(input('l(mm) 3.00 ?>'))
rh=toFloat(input('RH(Calculated by HallEffect.py) ?>'))
if d == 0:
    d = 0.5
if b == 0:
    b = 4
if l == 0:
    l = 3
if rh == 0:
    print('You MUST give RH')
    exit(1)
c6 = k * l * 10 / (b * d)
u = c6 * rh
print('6(o^-1 * cm^-1)=', c6, ', u(cm^2 * o^-1 * C^-1)=', u)
print('Deal with statistical dispersion by yourself.')
