#!/bin/env python3
import numpy

import sys
sys.path.append('..')
from quickmap import *

print('Usage: python va.py path/va-dat.in <Voltmeter range(V)> <Ammeter range(mA)> <fit line>')
print('Example: python3 va.py va-dat.in 1 15 true')
dat=numpy.loadtxt(sys.argv[1], delimiter=' ')
Uraw,Iraw=dat[:,0],dat[:,1]
U=[utrue/100*float(sys.argv[2]) for utrue in Uraw]
I=[itrue/150*float(sys.argv[3]) for itrue in Iraw]
if sys.argv[4] == 'true':
    GetMap(U,I,polyLine=True,poly_passO=True)
else:
    GetMap(U,I)
