# fyh2007
Python 100道常见题目编程

一、产生1,2,2,3,3,3,4,4,4,4,5,5,5,5规律的数列
old_list=[]
for i in range(1,12):
    for j in range(1,i):
        old_list.append(i-1)
print("原始数列如下:")
print(old_list)
new_list=[]
