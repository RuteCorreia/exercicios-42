#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s.ljust(8, 'Z'))

def main():
   
    if len(sys.argv) < 2:
        print("none")
        return
    
    # Process each argument
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()