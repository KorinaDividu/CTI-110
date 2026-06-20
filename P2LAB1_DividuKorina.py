#Korina Dividu
#06/21/2026
#P2LAB1_DividuKorina.py
#Calculate the diameter, circumference, and area of a circle

#Import with math module to use the constant, math.pi
import math

#Get the radius from user
radius = float(input("What is the radius of the circle? "))
print()

#Calculate diameter
diameter = 2 * radius

#Display diameter with  1 decimal point
print(f"The diameter of the circle is: {diameter:.1f}")

#Calculate circumference 
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"The circumference of the circle is: {circumference:.2f}")

#Calculate the area
area = math.pi * (radius**2)

#Display area with 3 decimal places
print(f"The area of the circle is: {area:.3f}")
