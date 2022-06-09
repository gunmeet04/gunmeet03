#Project1

print("Solving Q1:")
number = int(input("Enter any number: "))
print("binary equivalent of the number is",bin(number)[2:])

#Project2

print("Solving Q2:")
expression = input("Enter your expression: ")
print(eval(expression),end="\n")


# Project3

print("Solving Q3:")
import math
# (a)
print("a.",(3+4)*(5))
# (b)
n= float(input("Enter the value of n: "))
print("b.",n*(n-1)/2)
# (c)
r1=float(input("Enter the value of r1: "))
print("c.",4*math.pi*r1**2)
# (d)
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
r2=float(input("Enter the value of r2: "))
print("d.",math.sqrt(r2*(math.cos(a)**2) + r2*(math.sin(b)**2)))
# (e)
x1=float(input("Enter the value of x1: "))
x2=float(input("Enter the value of x2: "))
y1=float(input("Enter the value of y1: "))
y2=float(input("Enter the value of y2: "))
print("e.",(y2-y1)/(x2-x1), end="\n")

# Project4

print("Solving Q4:")
# (a)
for i in range(5):
    print(i,end=" ")
print()
# (b)
for i in range(3,10):
    print(i,end=" ")
print()
# (c)
for i in range(4,13,3):
    print(i,end=" ")
print()
# (d)
for i in range(15,5,-2):
    print(i,end=" ")
print()
# (e)
for i in range(5,3):
    print(i,end=" ")
print()


# Project5

print("Solving Q5:")
h= int(input("enter number of hydrogen atoms : "))
c= int(input("enter number of carbon atoms : "))
o= int(input("enter number of oxygen atoms : "))
d=(h*1.00794)+(c*12.0107)+(o*15.9994)
print("combined molecular weight of all atoms is :",d)
