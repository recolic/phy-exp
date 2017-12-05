#!/bin/env python3
# Type data into https://recolic.net/phy
# Edit&reuse it if you want.
# I'm making it print python code for other usage.
# Recolic Keghart.

import sys
if len(sys.argv) < 2:
    print('Usage: ./dataInput.py /path/to/dat/file | python')
    exit(123)

import numpy
dataset=numpy.loadtxt(sys.argv[1], delimiter=' ')
print('#!/bin/env python3')
print('# Warning: deprecated script!')
print('from pykeyboard import PyKeyboard')
print('import time')
print('k=PyKeyboard()')
oneLine=False
for ar in dataset:
    if type(ar) == numpy.float64:
        ar=dataset #fuck numpy......
        oneLine=True
    if len(ar) == 0:
        continue
    print('print(\'Waiting for 5 second... Please be ready for auto-typing.\')')
    print('time.sleep(5)')
    for i in ar:
        print('k.type_string(\''+ str(i) +'\')')
        print('k.tap_key(k.tab_key)')
    if oneLine:
        break
