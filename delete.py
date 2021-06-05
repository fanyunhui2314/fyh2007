a=[ ]
for i in range(0,10):
    x=int(input("输入第%d个数:"%(i+1)))
    a.append(x)
print("未删除前的数列:",end='')
for i in range(0,10):
          print(a[i],end='  ')
print(" ")
y=int(input("请输入要删除的一个数:"))
while y not in a:
    print("要删除的数是%d,该数不在原数列中!"%y,end='')
    y=int(input("请重新输入要删除的一个数:"))
a.remove(y)
print("%d这个数从数列中删除了"%y)
print("删除该数后的数列:",end='')
for i in range(0,9):
    print(a[i],end='  ')








