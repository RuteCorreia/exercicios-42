#!/usr/bin/env python3
def array_of_names(name_dict):
    # Initialize an empty list to hold the full names
    full_names = []
    
    # Iterate through each item in the dictionary
    for first_name, last_name in name_dict.items():
        # Capitalize the first and last names
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        # Append the full name to the list
        full_names.append(full_name)
    
    # Return the list of full names
    return full_names

# Example usage
name_dict = {
    'john': 'doe',
    'jane': 'smith',
    'alice': 'johnson'
}

print(array_of_names(name_dict))