# Programming Assignment_1
#Q1 Write a Python program to print "Hello Python"?

def first_program():
    return "Hello Python"

print(first_program())


#Q2 Write a Python program to do arithmetical operations addition and division.?


def add(num1,num2):
    return num1+num2

print(add(34,56))

def division(num1,num2):
    return num1//num2

print(division(45,5))


# Q3 Write a Python program to find the area of a triangle?


s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
s3 = float(input("Enter the third side: "))

def triangle(s1,s2,s3):
    s = (s1+s2+s3)/2
    area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5
    return (f"The area of triangle is {area}")
print(triangle(s1,s2,s3))


# Q4 Write a Python program to swap two variables?


x = 10 
y = 20 
print(f'The value before swap{x}')
print(f'The value before swap{y}')
temp = x
x = y
y = temp
print(f'The value after swap{x}')
print(f'The value after swap{y}')

#Q5 Write a Python program to generate a random number?

import random

x = random.randrange(1111,9999)
print(x)
