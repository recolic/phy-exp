#!/usr/bin/env python3

import sys
sys.path.append('..')
import quickmap

x,y = quickmap.DataFileToXYArray('without_damping.dat')
quickmap.GetMap(x,y,smoothLine=True)

x,y = quickmap.DataFileToXYArray('with_damping.dat')
quickmap.GetMap(x,y,smoothLine=True)


