#!/usr/bin/env python3
import sys


if len(sys.argv)  == 1 :
   estrutura = []
   i = 0
   j = 0

   while i <= 10:
      print(f"table de {i} :", end="")
      while j <= 10:
         print(f" {i * j} ", end="")
         j +=1
      print("")
      i +=1    
      j = 0  
else:
   print("none")        
      
   
