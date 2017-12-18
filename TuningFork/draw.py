#!/usr/bin/env python3

import sys
sys.path.append('..')
import quickmap
from quickmap import GetMultiMap, GetLine

x1,y1 = quickmap.DataFileToXYArray('without_damping.dat')
x2,y2 = quickmap.DataFileToXYArray('with_damping.dat')

GetMultiMap(GetLine(x1, y1, smoothLine=True) + GetLine(x2, y2, smoothLine=True))

sq_T = '14.633 19.327 24.256 29.192 34.589 39.547'.split(' ')
sq_T = [float(e) for e in sq_T]
m = [0,10,20,30,40,50]
quickmap.GetMap(m,sq_T,polyLine=True)
