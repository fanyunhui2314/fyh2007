s=1
i=1
while i<=10000000:
    s=s*((2*i)/(2*i-1)*(2*i)/(2*i+1))
    i=i+1
pi=2*s    
print("圆周率pi的值是:",pi)

    
