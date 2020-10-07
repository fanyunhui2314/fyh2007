# -*- coding: UTF-8 -*-
 
# Filename : 完数.py
# author by:fanyunhui2007
print("1000以内的完数有:",end="")
for i in range(2,1000):
     s=0
     for j in range(1,i-1):
          if i%j==0:
               s=s+j
               if  s==i:
                    print(i,end="   ")
    
    

    
    
    
         
     
