#!/usr/bin/python3

import pyperclip
import time
import sys

print('WARNING!!! This script will copy the contents of css/main.css into the system copy-paste buffer every second!')

while True:
  pyperclip.copy(open('css/main.css').read())
  print('.', end='')
  sys.stdout.flush()
  time.sleep(1)
