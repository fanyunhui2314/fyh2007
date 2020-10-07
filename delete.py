a=[ ]
for i in range(0,10):
    x=int(input("输入第%d个数:"%(i+1)))
    a.append(x)
print("未删除前的数列:",end='')
for i in range(0,10):
          print(a[i],end='  ')
print("\r")
y=int(input("请输入要删除的一个数:"))
if y in a:
    a.remove(y)
    print("删除该数后的数列:",end='')
    for i in range(0,9):
        print(a[i],end='  ')
elif y not in a:
    print("要删除的数是%d,该数不在原数列中!"%y,end='')
    for i in range(0,10):
        print(a[i],end='  ')
   







