#!/usr/bin/env python3
def greetings(name="noble stranger"):
    if  isinstance(name, str):
        print(f"Welcome, {name}!")
    else:
        print("Error! It was not a name.")


greetings("Alice")  
greetings()         
greetings(123)      