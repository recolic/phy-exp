#!/usr/bin/env python3

import sys
sys.path.append('..')
import quickmap

x31,y31=[2,4,8],[66.0,234,906]
x32,y32=[2,4,8],[22.3,85.1,341]
quickmap.GetMultiMap(quickmap.GetLine(x31, y31, polyLine=True, poly_passO=False) + quickmap.GetLine(x32, y32, polyLine=True, poly_passO=False))
