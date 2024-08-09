#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    
    input_string = sys.argv[1]
    
    if 'z' not in input_string:
        print("none")
        return
    
    for char in input_string:
        if char == 'z':
            print("z",end="")

if __name__ == "__main__":
    main()
 
     
     