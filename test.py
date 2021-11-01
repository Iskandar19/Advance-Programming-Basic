import math

#inserting the radius value
radius_str = input("Enter the radius : ")
radius_int = int(radius_str)

#calculating the circumference and area
circumference = 2* math.pi*radius_int
area = math.pi*(radius_int**2)

#print the area only
print ("The area is :", area)
