# Write a Python program that calculates the area of a circle based on the radius entered by the user.

def getArea():
    radius= float(input("Enter the radius: "))
    pie =3.14
    area = pie* radius **2 
    print ("area", area)
getArea()