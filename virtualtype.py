# Use this script with https://recolic.net/phy and https://recolic.net/phy2 
#     to avoid typing fucked numbers into page by hand.
from pykeyboard import PyKeyboard
import time

def virtual_type_array(arrToType, noWait=False):
    k = PyKeyboard()
    if not noWait:
        print('You have 5 seconds to ready for auto-typing.')
        time.sleep(5)
    for d in arrToType:
        k.type_string(str(d))
        k.tap_key(k.tab_key)
