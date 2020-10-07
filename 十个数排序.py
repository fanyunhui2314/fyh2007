arr = [ ]
for i in range(10):
    tmp = int(input("输入第%d个数:"%(i+1)))
    arr.append(tmp)
print("排序前的十个数:")
for i in range(10):
    print(arr[i],end=' ')
print("\r")
arr.sort()
print("十个数从小到大排序:\r")
for i in range(10):
    print(arr[i],end=' ')
print("\r")
print("十个数从大到小排序:")
for i in range(9,-1,-1):
    print(arr[i],end=' ')

