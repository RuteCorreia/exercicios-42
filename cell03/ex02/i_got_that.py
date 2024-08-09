#!/usr/bin/env python3
escreva = ""
escreva = input("What you gotta say? ")

while True:
    if escreva == 'stop':
        break
    else: 
       escreva = input("I got that! Anything else? :")
       print(escreva, end="")
       