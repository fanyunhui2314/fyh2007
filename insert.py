a=[ ]
for i in range(0,10):
    x=int(input("输入第%d个数:"%(i+1)))
    a.append(x)
print("未插入数前的数列:",end='')
for i in range(0,10):
          print(a[i],end='  ')
print("\r")
num=int(input("请输入要插入的一个数:"))
pos=int(input("请输入要插入的位置(pos<=10):"))
if pos<=10:
    a.insert(pos,num)
else:
    print("输入的数太大,请输入一个<=10的整数!")
    pos=int(input("请输入要插入的位置(pos<=10):"))
    a.insert(pos,num)
print("插入该数后的数列:",end='')
for i in range(0,11):
          print(a[i],end='  ')
print("\r")
a.sort()
print("重新排序后的数列:",end='')
for i in range(0,11):
          print(a[i],end='  ')



