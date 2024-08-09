#!/usr/bin/env python3
import sys

NumeroParametros =  len(sys.argv) - 1

if NumeroParametros > 0:
  print("Number of parameters:",sys.argv[1])
else:
    print("none")  