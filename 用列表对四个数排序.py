a=int(input("输入第一个数:"))
b=int(input("输入第二个数:"))
c=int(input("输入第三个数:"))
d=int(input("输入第四个数:"))
list1=[a,b,c,d]
print("排序前的四个数:")
for i in range(0,4):
    print("list1[{}]=".format(i),list1[i],"\x20",end='')
list1.sort()
print("\n")
print("排序后的四个数:")
for i in range(0,4):
    print("list1[{}]=".format(i),list1[i],"\x20",end='')
    

