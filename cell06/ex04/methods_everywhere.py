import sys

def shrink(s):
    """Displays the first eight characters of the string."""
    print(s[:8])

def enlarge(s):
    """Appends 'Z' characters to make the string a total of eight characters and displays it."""
    print(s.ljust(8, 'Z'))

def main():
    # Check if there are command-line arguments
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