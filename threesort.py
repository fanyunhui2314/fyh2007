raw=[]
for i in range(3):
    x=int(input('输入第%d个数: '%(i+1)))
    raw.append(x)
print("排序前的三个数:",end=' ')
for i in range(3):
    print(raw[i],end='  ')    
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print("\r")
print("升序后的三个数:",end=' ')
for i in range(3):
    print(raw[i],end='  ')
print("\r")
raw.sort(reverse=True)
print("降序后的三个数:",end=' ')
for i in range(3):
    print(raw[i],end='  ')
    
