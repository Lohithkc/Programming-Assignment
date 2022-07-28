#Q1 Write a Python Program to Find LCM?

n1 = int(input("Enter the First number: "))
n2 = int(input("Enter the Second number: "))

def lcm(a,b):
    if a > b:
        min_1 = a
    else:
        min_1 = b
    
    while True:
        if(min_1 % a == 0 and min_1 % b == 0):
            break
        min_1 = min_1 + 1
    return min_1

print(f"The L.C.M of {n1} and {n2} is {lcm(n1,n2)}")


#Q2 Write a Python Program to Find HCF?


x = int(input("Enter the First number: "))
y = int(input("Enter the Second number: "))

def hcf(x,y):
    if x > y:
        x, y = y, x
    for i in range(1,x+1):
        if (x % i == 0 and y % i == 0):
            hcf = i
        return i

print(hcf(x,y))

#Q3 Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

decimal = 566

print(f"In Binary {bin(decimal)}")
print(f"In Octal {oct(decimal)}")
print(f"In Hexadecimal {hex(decimal)}")


#Q4 Write a Python Program To Find ASCII value of a character?

c = input("Enter the character: ")
try:
    print(f"The ASCII vale of {c} is {ord(c)}")
except Exception as e:
    print("Enter the single letter or number like a or b or 1 or 6...")

#Q5 Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

n= int(input('Enter the number: '))
m = int(input('Enter the number: '))

add = lambda a,b: a+b
sub = lambda a,b: a-b
mul = lambda a,b: a*b
div = lambda a,b: a/b

print(add(n,m))
print(sub(n,m))
print(mul(n,m))
print(sub(n,m))
