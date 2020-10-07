a=list(range(5))
for i in range(0,5):
        a[i]=int(input("输入第{}个数:".format(i+1)))
print("排序前的五个数:")
for i in range(0,5):
        print(a[i],end=' ')
if a[0]>a[1]:
        a[0],a[1]=a[1],a[0]
if a[0]>a[2]:
        a[0],a[2]=a[2],a[0]
if a[0]>a[1]:
        a[0],a[3]=a[3],a[0]
if a[0]>a[4]:
        a[0],a[4]=a[4],a[0]
if a[1]>a[2]:
        a[1],a[2]=a[2],a[1]
if a[1]>a[3]:
        a[1],a[3]=a[3],a[1]
if a[1]>a[4]:
        a[1],a[4]=a[4],a[1]
if a[2]>a[3]:
        a[2],a[3]=a[3],a[2]
if a[2]>a[4]:
        a[2],a[4]=a[4],a[2]
if a[3]>a[4]:
        a[3],a[4]=a[4],a[3]
print("\r")
print("升序后的五个数:")
for i in range(0,5):
        print(a[i],end=' ')
print("\r")
print("降序后的五个数:")
for i in range(4,-1,-1):
        print(a[i],end=' ')



