# fyh2007
Python 100道常见题目编程

一、产生1,2,2,3,3,3,4,4,4,4,5,5,5,5规律的数列
# author:fyh2007
old_list=[]
for i in range(1,12):
    for j in range(1,i):
        old_list.append(i-1)
print("原始数列如下:")
print(old_list)
new_list=[]
二、产生1,2,2,3,3,3,4,4,4,4,5,5,5,5规律的数列并且删除多余的数
# author:fyh2007
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
三、产生1,1,2,1,2,3,1,2,3,4,1,2,3,4,5规律的数列
# author:fyh2007
old_list=[]
for i in range(1,12):
    for j in range(1,i):
        old_list.append(j)
print("原始数列如下:")
print(old_list)
