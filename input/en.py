#!/bin/env python
# It helps me to copy English answer really quick!

import sys
if len(sys.argv) < 3:
    print('Usage: ./dataInput.py /path/to/dat/file \'delimiter\' | python')
    exit(123)

fd=open(sys.argv[1],'r')
ar=fd.read().replace('\n','').replace('\'','\\\'').replace('’','\\\'').split(sys.argv[2])
fd.close()

print('#!/bin/env python3')
print('from pykeyboard import PyKeyboard')
print('import time')
print('k=PyKeyboard()')
print('print(\'Waiting for 5 second... Please be ready for auto-typing.\')')
print('time.sleep(5)')
for i in ar:
    if len(i) == 0:
        continue
    print('k.type_string(\''+i+'\')')
    print('k.tap_key(k.tab_key)')

