# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:51:19 2019

@author: STEM
"""

def cadbury(a):
    cadbury =a+10+5
    print(cadbury)
    
cadbury(5)



"""
def cadbury(a,b,c):
    cadbury ="Milk Choclate","Dark Chocolate","White Chocolate
    print(cadbury)
    
cadbury("Milk Chocolate", "Dark Chocolate","White Chocolate")


def cadbury(a):
    cadbury ="Milk Chocolate"
    print
"""

cadbury1 = "Milk Chocolate"
cadbury2 = "Dark Chocolate"
cadbury3 = "White Chocolate"

def ReadType(a):
    print("The type of chocolate is ",a )
    
ReadType(cadbury1) 

def ReadType(b):
    print("The type of chocolate is", b)
    
ReadType(cadbury2)

def ReadType(c):
    print("The type of chocolate is", c)
    
ReadType(cadbury3)


def cadburyBox(w,d,m):
    print("There is",m,",",d,",",w,"in the box")
    
cadburyBox("White Chocolate", "Dark Chocolate", "Milk Chocolate")


#gret a person by their name

print("Hello Chris")

a ="Kaya"
print("Hello",a)


name = input("please enter your name")

print("Your name is", name)

age = input("please enter your age")

print("Thank you. You entered", age)

ageint = int(age)
ageint

ageint = float(age)

import math

dir(math)


math.pi

math.factorial(12)
math.factorial(0)
math.pow(6,15)
    

def CubicRoot(a):
    print("The cubic root of",a,"is",math.pow(a,(1/3)))

CubicRoot(8)

n=int(3)
d=int(9)
x=1/n
print("you answer=",d**x)

def cubic(x):
    cubic= math.pow(x,.33)
    print("The cubic rooot of" ,x, "is" ,cubic,)
    
cubic(8)



def CubicRoot(x):
    result= math.pow(x,1/3)
    print("The  root of" ,x, "is" ,result)
    
CubicRoot(8)

UserInput= int(input("Enter a value to find its cubic root:"))

CubicRoot(UserInput)


def Squareroot(n):
    result= math.pow(n,1/2)
    print("The squareroot of" ,n, "is", result)
    
Squareroot(100)

Input= int(input("Enter a value to find its squareroot:"))

Squareroot(Input)



    


