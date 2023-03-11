# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 11:59:33 2023

@author: norbe
"""

import sys

FILENAME = sys.argv[1]
count = 0
with open(FILENAME, "rt", encoding="utf8") as f:
        for data in f:
            text = data.strip()
            for t in text:
                if t == "e":
                    count += 1
        print(count)