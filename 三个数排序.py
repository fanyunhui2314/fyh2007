a=int(input("输入第一个数:"))
b=int(input("输入第二个数:"))
c=int(input("输入第三个数:"))
print("排序前的三个数:")
print("a=%d,b=%d,c=%d"%(a,b,c))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print("排序后的三个数:")            
print("a=%d,b=%d,c=%d"%(a,b,c))

