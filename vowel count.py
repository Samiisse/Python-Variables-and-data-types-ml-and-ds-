#Create a function to count the number of vowels in a given string

def count_vowels(string):
    # Convert the input string to lowercase to handle both upper and lower case vowels
    string = string.lower()
    
    # Define a set of vowels
    vowels = "aeiou"
    
    # Initialize a variable to count the vowels
    count = 0
    
    # Iterate through the characters in the string
    for char in string:
        if char in vowels:
            count += 1

    return count

# Example usage:
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is {vowel_count}.")

