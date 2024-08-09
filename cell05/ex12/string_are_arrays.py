#!/usr/bin/env python3

import sys

inputArgs = sys.argv 
i= 1

if len(inputArgs) > 1:
   
   repeticao =  inputArgs[1].count("z")
   while i <= repeticao:
       print("z", end="")
       i +=1   
 
     
     