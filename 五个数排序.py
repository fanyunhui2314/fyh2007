a=int(input("输入第一个数:"))
b=int(input("输入第二个数:"))
c=int(input("输入第三个数:"))
d=int(input("输入第四个数:"))
e=int(input("输入第五个数:"))
print("排序前的五个数:")
print("a=%d,b=%d,c=%d,d=%d,e=%d"%(a,b,c,d,e))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if a>d:
    a,d=d,a    
if a>e:
    a,e=e,a    
if b>c:
    b,c=c,b
if b>d:
    b,d=d,b
if b>e:
    b,e=e,b    
if c>d:
    c,d=d,c
if c>e:
    c,e=e,c
if d>e:
    d,e=e,d            
print("排序后的五个数:")            
print("a=%d,b=%d,c=%d,d=%d,e=%d"%(a,b,c,d,e))

