# Programming Assignment_3

#Q1 Write a Python Program to Check if a Number is Positive, Negative or Zero?

num = int(input("Enter the number: "))

def number(num):
    if num > 0:
        print(f"The number {num} is Positive")
    elif num < 0:
        print(f"The number {num} is Negative")
    else:
        print(f"The number {num} is Zero")

number(num)


#Q2 Write a Python Program to Check if a Number is Odd or Even?


num = int(input("Enter the number: "))

def check(num):
    if num % 2 == 0:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")

check(num)


#Q3 Write a Python Program to Check Leap Year?


year = int(input('Enter year : '))

def leap(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

leap(year)


#Q4 Write a Python Program to Check Prime Number?


num = int(input("Enter the number: "))

def prime(num):
    for i in range(2,num + 1):
        if num % i == 0:
            break
    if num == i:
        return(f"The {num} is prime")
    else:
        return(f"The {num} is not prime")
print(prime(num))


#Q5 Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


def prime():

    for i in range(1,10001):
        if i % 2 == 0:
            print(f"The number {i} is not prime")
        else:
            print(f"The number {i} is prime")
prime()