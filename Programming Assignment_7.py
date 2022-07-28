# Write a Python Program to find sum of array?

def array():
    l = []
    for i in range(11):
        l.append(i)
    print(l)

    sum = 0 
    for i in l:
        sum = sum + 1
    return f"The sum of arrary is {sum}"

print(array())

# Write a Python Program to find largest element in an array?

def largest():
    l = []
    for i in range(11):
        l.append(i)
    print(l)

    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i
    print(f"The largest number is {max_num}")

largest()


# Write a Python Program for array rotation?

arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2

def SplitArray(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = x		

SplitArray(arr, n, position)
for i in range(0, n):
	print(arr[i], end = ' ')


# Write a Python Program to check if given array is Monotonic?

A = [56,55,44,34,20]
def isMonotonic(A):
 
    return (all(A[i] <= A[i + 1] 
            for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] 
            for i in range(len(A) - 1)))
 
print(isMonotonic(A))