#!/usr/bin/env python3
import sys

inputArgs = sys.argv 
i = 1
repeticao = len(inputArgs) - 1

if len(inputArgs) > 1:

    param =  inputArgs[i].count("ism") 

    while i <= repeticao:        
        if "ism" not in inputArgs[i]:
           print(inputArgs[i] + "ism")
        else:  
            print(inputArgs[i])  
        i +=1  
else:
   print("none")               

