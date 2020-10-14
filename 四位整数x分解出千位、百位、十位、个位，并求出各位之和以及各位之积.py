x=int(input("请输入一个四位数(1000<x<10000):"))
a=int(x/1000)
b=int((x%1000)/100)
c=int(((x%1000)%100)/10)
d=x-1000*a-100*b-10*c
print("%d+%d+%d+%d=%d"%(a,b,c,d,a+b+c+d))
print("%d×%d×%d×%d=%d"%(a,b,c,d,a*b*c*d))
