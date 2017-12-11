#!/usr/bin/env python3

import sys
sys.path.append('..')
import quickmap

x,y = quickmap.DataFileToXYArray('without_damping.dat')
quickmap.GetMap(x,y,smoothLine=True)

x,y = quickmap.DataFileToXYArray('with_damping.dat')
quickmap.GetMap(x,y,smoothLine=True)

sq_T = '14.633 19.327 24.256 29.192 34.589 39.547'.split(' ')
sq_T = [float(e) for e in sq_T]
m = [0,10,20,30,40,50]
quickmap.GetMap(m,sq_T,polyLine=True)
