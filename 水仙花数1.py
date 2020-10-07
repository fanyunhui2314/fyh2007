# -*- coding: UTF-8 -*-
 
# Filename : 水仙花数.py
# author by:fanyunhui2007
print("水仙花数如下:")
for i in range(100,1000):
     a=int(i/100)
     b=int((i-100*a)/10)
     c=int(i-100*a-10*b)
     if (a**3+b**3+c**3)==i:
        print("%d×100+%d×10+%d="%(a,b,c),i)
    
    

    
    
    
         
     
