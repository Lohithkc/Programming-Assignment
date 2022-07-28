# Programming Assignment_4

#Q1 Write a Python Program to Find the Factorial of a Number?

num = int(input("Enter the number: "))

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num -1)
print(factorial(num))


#Q2 Write a Python Program to Display the multiplication Table?

num = int(input("Enter the number: "))

for i in range(11):
    print (f"{num} * {i} = {num * i}")



#Q3 Write a Python Program to Print the Fibonacci sequence?

num = int(input("Enter the Range Number: "))
def Fibonacci():
    a = 0
    b = 1
    for i in range(0,num):
        if(i <=1):
            next = i
        else:
            next = a + b
            a = b
            b = next
        print(next)
Fibonacci()



# Write a Python Program to Find the Sum of Natural Numbers?


num = int(input("Enter the natural number: "))

def natural(num):
    if num > 0:
        sum = 0
        for i in range(1,num +1):
            sum = sum + i
        print(sum)
    else:
        print("Enter the +ve number")
natural(num)