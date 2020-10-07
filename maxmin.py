# -*- coding: UTF-8 -*-
 
# Filename : maxmin.py
# author by:fanyunhui2007
a=list(range(10))
for i in range(0,10):
    a[i] = int(input("请输入第{}数:".format(i+1)))
for i in range(0,10):    
    print ("a["+str(i)+"]={}".format(a[i]))
zuidashu=a[0]
for i in range(1,10):
    if a[i]>zuidashu:
        zuidashu=a[i]
zuixiaoshu=a[0]        
for j in range(1,10):
    if a[j]<zuixiaoshu:
        zuixiaoshu=a[j]
print("最大的数是: {}".format(zuidashu))
print("最小的数是: {}".format(zuixiaoshu))
print("第"+str(a.index(min(a))+1)+"个数是最小数")
print("第"+str(a.index(max(a))+1)+"个数是最大数")
     
