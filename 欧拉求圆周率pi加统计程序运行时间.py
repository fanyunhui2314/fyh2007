from math import sqrt
import time
start = time.time()
s=0
i=1
item=1
while item>0.000000000000001:
    s=s+item
    i=i+1
    item=1/(i*i)
pi=sqrt(6*s)
print("圆周率pi的值是:",pi)
end = time.time()
print("程序运行了%6.2f"%(end-start),"秒")
