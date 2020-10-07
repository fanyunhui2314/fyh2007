#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=0
b=1
while  (b<1000) :
    print(b,end="  ")
    t=a
    a=b
    b=t+b
print("\n")    
