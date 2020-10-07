import math as ma
print("100以内的勾股数有:")
print("  a      b       c       ")
count=0
for a in  range(1,101):
    for b in range(a+1,101):
        c=int(ma.sqrt(a*a+b*b))
        if ((c*c==a*a+b*b) and (a+b>c) and (a+c>b) and (b+c>a) and c<100):
            print("%3d    %3d     %3d"%(a,b,c))
            count=count+1
            if count%5==0:
                print("\n")
 

            
            
