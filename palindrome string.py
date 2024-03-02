#Implement a program that checks if a given string is a palindrome

def palindrom_str(input_string):
    cleaned_string = input_string.replace("" "" , "").lower() # Remove spaces and convert the input to lowercase
    return cleaned_string == cleaned_string [::-1]  # Reverse the cleaned string and compare it with the original

# Input string to check
input_string = input("Enter a string to check if it's a palindrome: ")

if palindrom_str(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
