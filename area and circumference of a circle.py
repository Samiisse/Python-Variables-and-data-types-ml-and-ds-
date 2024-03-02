#Calculate the area and circumference of a circle given its radius

import math

def calculate_circle_area(radius):
    area = math.pi * (radius**2)
    return area

def calculate_circumference_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input('Enter the radius: '))

circle_area = calculate_circle_area(radius)
circumference_circle = calculate_circumference_circle(radius)

print(f"The area of a circle with radius {radius} is {circle_area: 2f}")
print(f"The circumference of a circle with radius {radius} is {circumference_circle: .2f}")



