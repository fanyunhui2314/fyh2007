a=int(input("输入第一个数:"))
b=int(input("输入第二个数:"))
c=int(input("输入第三个数:"))
d=int(input("输入第四个数:"))
print("排序前的四个数:")
print("a=%d,b=%d,c=%d,d=%d"%(a,b,c,d))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if a>d:
    a,d=d,a    
if b>c:
    b,c=c,b
if b>d:
    b,d=d,b
if c>d:
    c,d=d,c    
print("排序后的四个数:")            
print("a=%d,b=%d,c=%d,d=%d"%(a,b,c,d))

