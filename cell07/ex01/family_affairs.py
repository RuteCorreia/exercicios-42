#!/usr/bin/env python3
def find_the_redheads(family_dict):
    # Use filter to find the keys (names) with the value 'red'
    redheads = list(filter(lambda name: family_dict[name] == 'red', family_dict))
    
    # Return the list of names with red hair
    return redheads

# Example usage
family_dict = {
    'Alice': 'blonde',
    'Bob': 'red',
    'Charlie': 'brunette',
    'Diana': 'red',
    'Eve': 'black'
}

print(find_the_redheads(family_dict))