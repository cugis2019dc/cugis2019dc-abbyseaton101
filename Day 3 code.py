# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:16:55 2019

@author: STEM
"""

Cadburymilk="Cadburymilk=5"
Cadburydark="Cadburydark=3"
Cadburywhite="Cadburywhite=8"

def Cadburybox(a,b,c):
    print(Cadburymilk, Cadburydark,Cadburywhite)
    
Cadburybox(Cadburymilk,Cadburydark,Cadburywhite)

Darkchocolate = 5
Milkchocolate = 6
Whitechocolate = 8
print(Whitechocolate)
print(Darkchocolate)
print(Milkchocolate)

cadburryType1="and 6 milk chocolates"
cadburryType2="5 dark chocolates"
cadburryType3="8 white chocolates"
def cadburrybox(m,d,w):
    print("there are ",m,"," ,d, w, "in the box")
    
cadburrybox(cadburryType1,cadburryType2,cadburryType3)

chocolate1 = {"cadburymilk" :5}
chocolate2 = {"cadburydark" :8}
chocolate3 = {"cadburywhite" :3}
chocolate1
chocolate2
chocolate3

chocolatebox ={"dark":5,"milk":6,"white":8}
chocolatebox



nameage={"Steve":32, "Lia":28, "Vin":45, "Katie":38}
    
nameage = {"Steve":32}
nameage = {"Lia":28}
nameage = {"Vin":45}
nameage = {"Katie":38}


studentage ={"steve":32, "Lia":28, "Vin":45, "Katie":38}
studentage

studentgender = {"steve":"M", "Lia":"F", "vin":"M", "Katie":"F"}
studentgender

#list
studentlist = [ ['steve',32,'M'], ["lia",28,"F"], ["Vin",45,"M"],["katie",38,"F"]]
studentlist

student = [studentage,studentgender]
student

import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentlist,columns =("name","age","gender"))
studentdf
studentdf["name"]
studentdf["age"]


namequantity = {"milk":5}
namequantity = {"dark":8}
namequantity = {"white":3}

chocolates = [ ["milk",5,],["dark",8],["white",3]]
chocodf = pandas.DataFrame(chocolates, columns=("chocolate", "quantity"))
print(chocodf)














