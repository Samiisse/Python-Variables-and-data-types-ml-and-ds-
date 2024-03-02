#Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)

import string

def is_pangram(input_string):
    # Remove spaces and convert the input to lowercase
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Create a set of all lowercase letters
    alphabet_set = set(string.ascii_lowercase)
    
    # Check if the set of letters in the cleaned string is equal to the alphabet set
    return set(cleaned_string) == alphabet_set

# Input string to check
input_string = input("Enter a string to check if it's a pangram: ")

if is_pangram(input_string):
    print(f"'{input_string}' is a pangram.")
else:
    print(f"'{input_string}' is not a pangram.")
