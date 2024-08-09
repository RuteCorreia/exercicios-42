#!/usr/bin/env python3
import sys

inputArgs = sys.argv 

if len(inputArgs) > 1:
    x = list(range(int(inputArgs[1]), int(inputArgs[2])))
    print(x,end=" ")
else: 
    print("none")    