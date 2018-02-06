#!/usr/bin/env python

import sys
import ipaddress

try:
    ranges = [ipaddress.ip_network(arg) for arg in sys.argv[1:]]
except ValueError as e:
    print("Error:", e)
    sys.exit(1)

clean = True

for x in range(len(ranges)-1):
    for y in range(x+1, len(ranges)):
        if ranges[x].overlaps(ranges[y]):
            print("Overlap Found Between -", ranges[x], "and", ranges[y])
            clean=False

if clean == True:
    print("No overlaps found in given ranges!")
