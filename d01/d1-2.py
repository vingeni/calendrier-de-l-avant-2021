#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

import sys

count = 0
prev = None
l = []

myinput = sys.stdin

for line in myinput:
    i = int(line)
    l.append(i)
    l = l[-3:]
    if (len(l) < 3):
        continue
    s = sum(l)
    if (prev != None and prev < s):
        count = count + 1
    prev = s

print(count)
