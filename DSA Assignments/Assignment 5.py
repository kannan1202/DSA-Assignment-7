"""
Question 1: Compute and return the square root of x, where x is guaranteed to be a non-negative
integer. And since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned. Also, talk about the time complexity of your
code.

"""
# Time complexity O(1)
import math
def SquareRoot(num):
    return int(math.sqrt(num))

num = int(input("Enter a number to compute square root: "))
result = SquareRoot(num)
print(f"The square root of {num} is {result}")


"""
Question 2: You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.

"""
# Time complexity O(logn), because by using binary search we divide the array everytime by 2,
# So we get the time complexity as logn to the base 2,when solved using substitution method or Master's theorem.
def FirstBadOne(Version,left,right):
    if left == right:
        return left
    else:
        while left<=right:
            middle = left +(right - left)//2
            if Version[middle] == 0:
                return FirstBadOne(Version,middle+1,right)
            else:
                return FirstBadOne(Version,left,middle-1)

Version = [0,0,0,1,1,1,1,1,1]
left = 0
right = len(Version)-1
result = FirstBadOne(Version,left,right)
print(f"The index of the first bad version is {result}")

"""
Question 3: Given a positive integer num, write a program that returns True if num is a perfect
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code.
"""
#Time complexity O(n)
def PerfectSquare(num):
    for i in range(1,num+1):
        if i*i == num:
            return True
    else:
        return False

num = int(input("Enter the number: "))
result = PerfectSquare(num)
if result == True:
    print(f"{result},{num} is a perfect square.")
else:
    print(f"{result},{num} is not a perfect square.")










