# -*- coding: UTF-8 -*-
 
# Filename : 歌手成绩.py
# author by:fanyunhui2007
a=list(range(10))
for i in range(0,6):
    a[i] = int(input("请输入歌手第{}个成绩：".format(i+1)))
print (a[i])
max=a[0]
min=a[0]
for i in range(1,6):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
s=0
for i in range(0,6):
    s=s+a[i]
aver=(s-min-max)/4
print("去掉一个最高分 :{}".format(max))
print("去掉一个最低分 :{}".format(min))
print("歌手最后得分:{}".format(aver))

         
     
