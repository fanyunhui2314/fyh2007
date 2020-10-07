a=int(input("输入第一个数:"))
b=int(input("输入第二个数:"))
print("a=%d,b=%d"%(a,b))
if a<b:
    a,b=b,a
m=a*b
c=a%b
while (c!=0):
    a=b
    b=c
    c=a%b
print("a和b最大公约数是:%d"%b)
print("a和b最小公倍数是:%d"%(m/b))
