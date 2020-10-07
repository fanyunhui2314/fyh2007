print("输入三个数:")
a=int(input("输入第一个数a的值:"))
b=int(input("输入第二个数b的值:"))
c=int(input("输入第三个数c的值:"))
print("a=%d,b=%d,c=%d"%(a,b,c))
max=a
if (max<b):
    max=b
if (max<c):
    max=c
print("三个数中最大的数是:%d"%max)
min=a
if (min>b):
    min=b
if (min>c):
    min=c
print("三个数中最小的数是:%d"%min)


