#!/usr/bin/python3
import sys
sumy = 0
for i in range(1, len(sys.argv)):
    sumy += int(sys.argv[i])
print(sumy)
