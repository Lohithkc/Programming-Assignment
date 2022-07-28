# Programming Assignment_2
#Q1 Write a Python program to convert kilometers to miles?

km = int(input("Enter the value in kilometer: "))
diff = .621
def concert(km,diff):
    miles = km * diff
    return (f"{km} kilomere is equal to {miles} miles ")
print(concert(km,diff))


#Q2 Write a Python program to convert Celsius to Fahrenheit?


celsius = int(input("Enter the temperature: "))

def temp(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return (f"The temp in celsius {celsius} C into fahrenheit {fahrenheit} F")
print(temp(celsius))


#Q3 Write a Python program to display calendar?


import calendar

c = calendar.calendar(2021)
print(c)


#Q4 Write a Python program to solve quadratic equation?


import cmath

a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(f'The solution are {sol1} and {sol2}')


#Q5 Write a Python program to swap two variables without temp variable?


x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))

def swap(x,y):
    print(f"Before swapping {x} and {y}")
    x,y = y,x
    print(f"After swapping {x} and {y}")
swap(x,y)