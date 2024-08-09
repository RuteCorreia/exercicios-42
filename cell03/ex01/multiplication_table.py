#!/usr/bin/env python3
def new_func():
    tabuada= int(input("Enter a number: "))

    for count in range(9):
        print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))

new_func()