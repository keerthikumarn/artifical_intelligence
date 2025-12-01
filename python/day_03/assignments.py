import math

# Declare your age as an integer variable
age = 40

# Declare your height as a float variable
height = 5.8

# Declare a variable that stores a complex number
complex_number = 3 + 4j

# Prompt the user to enter base and height of a triangle and calculate its area
#base = float(input("Enter the base of the triangle: "))
#tri_height = float(input("Enter the height of the triangle: "))
base = 30
tri_height=15
area = 0.5 * base * tri_height
print("The area of the triangle is:", area)

'''
Compute the perimeter of the triangle
'''
side_a = float(input("Enter the side A of the triangle: "))
side_b = float(input("Enter the side B of the triangle: "))
side_c = float(input("Enter the side C of the triangle: "))

perimeter = side_a + side_b + side_c
print("Perimeter of the triangle is: ", perimeter)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

# Euclidean Distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", slope)
print("Euclidean Distance:", distance)

