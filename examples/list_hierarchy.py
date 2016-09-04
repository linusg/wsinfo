# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(1, os.path.abspath('..'))
from wsinfo import Info

w = Info("http://localhost/")
indent = "  "
for nr, text in w.hierarchy:
    print(indent*(int(nr[1])*len(indent)-len(indent)) + "└> " + text)
