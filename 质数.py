# -*- coding: UTF-8 -*-
 
# Filename : 质数.py
# author by:fanyunhui2007
print("100以内的质数有:",end="")
num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)

    
    

    
    
    
         
     
