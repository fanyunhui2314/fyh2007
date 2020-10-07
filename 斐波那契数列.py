# -*- coding: UTF-8 -*-
 
# Filename : 斐波那契数列.py
# author by:fanyunhui2007
n=int(input("输入斐波那契数列的项数:"))
a=list(range(n))
a[0]=1
a[1]=1
for i in range(2,n):
   a[i]=a[i-1]+a[i-2]

for i in range(0,n):
  print (a[i],end="  ")
  
    

    
    
    
         
     
