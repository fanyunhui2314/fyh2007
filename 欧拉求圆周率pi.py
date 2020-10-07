from math import sqrt
i=1
s=0
item=1
while item>0.000000000000001:
    s=s+item
    i=i+1
    item=1/(i*i)
pi=sqrt(6*s)
print("圆周率pi的值是:",pi)
