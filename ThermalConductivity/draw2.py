#!/usr/bin/env python3

time = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480]
tc = [43.2, 42.9, 42.5, 42.2, 41.9, 41.5, 41.2, 40.9, 40.5, 40.3, 40.0, 39.7, 39.4, 39.1, 38.8, 38.5, 38.2]

import sys
sys.path.append("..")
import quickmap

quickmap.GetMap(time, tc, line=True)
