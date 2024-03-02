#Implement a program that converts a given number of minutes into hours and minutes

def convert_minutes_hours_and_minutes(minutes): # Function to convert minutes to hours and remaining minutes
    hours = minutes // 60                       # 1 hour has 60 minutes
    remaining_minutes = minutes % 60            # Remaining minutes
    return hours, remaining_minutes

# Get input from the user
try:
    minutes = int(input("Enter the number of minutes: "))
    if minutes < 0:
        print("Please enter a non-negative number of minutes.")
    else:
        hours, remaining_minutes = convert_minutes_hours_and_minutes(minutes)
        if hours == 1 and remaining_minutes == 1:
            print(f"{minutes} minutes is equal to {hours} hour and {remaining_minutes} minute.")
        elif hours == 1:
            print(f"{minutes} minutes is equal to {hours} hour and {remaining_minutes} minutes.")
        elif remaining_minutes == 1:
            print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minute.")
        else:
            print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")
except ValueError:
    print("Invalid input. Please enter a valid number of minutes.")


