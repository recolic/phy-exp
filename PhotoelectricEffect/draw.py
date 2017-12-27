#!/usr/bin/env python3

import sys
sys.path.append('..')
import quickmap

x1,y1 = quickmap.DataFileToXYArray('calc_h.dat')
quickmap.GetMap(x1,y1,polyLine=True)

x21, y21 = quickmap.DataFileToXYArray('IU1.csv', wordDelimiter = ',')
x22, y22 = quickmap.DataFileToXYArray('IU2.csv', wordDelimiter = ',')
x23, y23 = quickmap.DataFileToXYArray('IU3.csv', wordDelimiter = ',')
quickmap.GetMultiMap(quickmap.GetLine(x21, y21, smoothLine=True) + quickmap.GetLine(x22, y22, smoothLine=True) + quickmap.GetLine(x23, y23, smoothLine=True))


#x1, y1 = quickmap.DataFileToXYArray('1.csv', wordDelimiter = ',')
#quickmap.GetMap(x1, y1, polyLine=True)
#
#x21, y21 = quickmap.DataFileToXYArray('2-1.csv', wordDelimiter = ',')
#x22, y22 = quickmap.DataFileToXYArray('2-2.csv', wordDelimiter = ',')
#x23, y23 = quickmap.DataFileToXYArray('2-3.csv', wordDelimiter = ',')
#quickmap.GetMultiMap(quickmap.GetLine(x21, y21, smoothLine=True) + quickmap.GetLine(x22, y22, smoothLine=True) + quickmap.GetLine(x23, y23, smoothLine=True))
#
#x31, y31 = quickmap.DataFileToXYArray('3-1.csv', wordDelimiter = ',')
#x32, y32 = quickmap.DataFileToXYArray('3-2.csv', wordDelimiter = ',')
#quickmap.GetMultiMap(quickmap.GetLine(x31, y31, polyLine=True) + quickmap.GetLine(x32, y32, polyLine=True))
