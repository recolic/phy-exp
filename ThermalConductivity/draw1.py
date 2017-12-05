#!/usr/bin/env python3

minutes = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92]
rawTa = [18.7, 36.0, 47.8, 50.2, 50.3, 50.2, 50.3, 50.4, 50.4, 50.5, 50.5, 50.5, 50.5, 50.6, 50.5, 50.6, 50.5, 50.7, 50.8, 50.8, 50.8, 50.8, 50.8, 50.8, 50.9, 50.9, 50.9, 50.9, 50.9, 50.9, 50.9, 50.9, 50.9, 51.0, 51.0, 51.0, 51.1, 51.1, 51.1, 51.1, 51.1, 51.1, 51.1, 51.1, 51.1, 51.2, 51.2]
rawTa = [Ti - 0.3 for Ti in rawTa]
rawTc = [19.4, 19.4, 20.0, 21.6, 23.3, 25.0, 26.8, 28.3, 29.4, 30.7, 31.8, 32.9, 33.5, 34.3, 34.9, 35.6, 36.1, 36.7, 37.0, 37.5, 37.8, 38.2, 38.5, 38.8, 39.0, 39.3, 39.5, 39.6, 39.8, 39.9, 40.1, 40.2, 40.3, 40.4, 40.6, 40.6, 40.7, 40.8, 40.8, 40.9, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0]

import sys
sys.path.append("..")
import quickmap

##for powerTest in range(16):
##    quickmap.GetMap(minutes, rawTa, line=True, maxXPower=powerTest)#, inverseK=True)
##for powerTest in range(16):
##    quickmap.GetMap(minutes, rawTa, line=True, maxXPower=powerTest, inverseK=True)
#for powerTest in range(16):
#    print(">>>", powerTest)
#    quickmap.GetMap(minutes, rawTc, line=True, maxXPower=powerTest)#, inverseK=True)
##for powerTest in range(16):
##    quickmap.GetMap(minutes, rawTc, line=True, maxXPower=powerTest, inverseK=True)
quickmap.GetMap(minutes, rawTa)
quickmap.GetMap(minutes, rawTc, line=True, maxXPower=9)