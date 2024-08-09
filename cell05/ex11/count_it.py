#!/usr/bin/env python3
import sys

inputArgs = sys.argv 

print ("parameters: " ,len(inputArgs) - 1)

for i in range(1, len(inputArgs)):
    print(sys.argv[i], ": ", len(sys.argv[i],))