old_list=[]
for i in range(1,12):
    for j in range(1,i):
        old_list.append(i-1)
print("原始数列如下:")
print(old_list)
for i in range(1,11):
    cishu=old_list.count(i)
    print("%d一共有%d个"%(i,cishu))
