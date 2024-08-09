#!/usr/bin/env python3
x1 = float(input('Give me a number: '))

def valor(v):
  n = int(v)
  m = v * 10
  s = n * 10
  if m == s:
    return ('This number is an integer.'.format(v))#retorn 1
  else:
    return ('This number is a decimal'.format(v))#retorn 2 
r = valor(x1)
print(r)