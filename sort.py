# -*- coding: UTF-8 -*-
 # Filename : sort.py
# author by:fanyunhui2007
a=list(range(10))
print ("输入十个整数")
for i in range(0,10):
    a[i] = int(input("请输入第{}数：".format(i+1)))
print("排序前的十个数:")
for i in range(0,10):
    print (a[i],end="   ")
print( )
for i in range(0,10):
 for j in range(i+1,10):
         if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("排序后的结果如下:")            
for i in range(0,10):        
    print (a[i],end="   ")
print

    

    
    
    
         
     
