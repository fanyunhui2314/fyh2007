x=int(input("输入一个三位整数:"))
a=int(x/100)
b=int((x%100)/10)
c=x-100*a-10*b
s=a+b+c
p=a*b*c
print("%d+%d+%d=%d"%(a,b,c,s))
print("%d×%d×%d=%d"%(a,b,c,p))


