old_list=[]
for i in range(1,12):
    for j in range(1,i):
        old_list.append(i-1)
print("原始数列如下:")
print(old_list)
new_list=[]
for each in old_list:
    if each not in new_list:
        new_list.append(each)
print("删除多余数后的数列如下:")
print(new_list)
