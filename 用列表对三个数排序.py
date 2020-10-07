a=list(range(3))
print ("输入三个整数")
for i in range(0,3):
    a[i] = int(input("请输入第{}数:".format(i+1)))
print("排序前的三个数:")
for i in range(0,3):
    print ("a[{}]=".format(i),a[i],end='  ')
print( )
print("排序后的三个数:")
a.sort()
for i in range(0,3):
    print ("a[{}]=".format(i),a[i],end='  ')

