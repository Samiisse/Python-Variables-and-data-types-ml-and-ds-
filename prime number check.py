#Write a program to check if a number is prime

def is_prime(number):
    if number <= 1:
        return False  # 1 and any number less than 1 are not prime

    if number <= 3:
        return True  # 2 and 3 are prime

    if number % 2 == 0 or number % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime

    # Check for prime by testing divisors up to the square root of the number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Get input from the user
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
