x=list(range(10))
for i in range(10):
    x[i]=int(input("输入第%d个数:"%(i+1)))
for i in range(0,10):
    for j in range(i+1,10):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print("升序排序:")
for i in range(0,10):
    print(x[i],end='  ')
for i in range(0,10):
    for j in range(i+1,10):
        if x[i]<x[j]:
            x[i],x[j]=x[j],x[i]
print("\r")
print("降序排序:")
for i in range(0,10):
    print(x[i],end='  ')
    
