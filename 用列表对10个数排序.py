raw=[]
for i in range(10):
    x=int(input('输入第%d个数:'%(i+1)))
    raw.append(x)
print("排序前的10个数:",end=' ')
for i in range(10):
    print(raw[i],end='  ')
print("\r")
raw.sort()
print("升序排列后的10个数:",end=' ')
for i in range(10):
    print(raw[i],end='  ')
print("\r")
raw.sort(reverse=True)
print("降序排列后的10个数:",end=' ')
for i in range(10):
    print(raw[i],end='  ')
