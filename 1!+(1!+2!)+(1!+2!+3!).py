## 计算1!+(1!+2!)+(1!+2!+3!)这样规律的数列的和
## author:fyh2007
sum=0
n=int(input("输入n的值:"))
for i in range(1,n+1):
    p=1
    for j in range(1,i+1):
        p=p*j
        sum=sum+p
print("sum=",sum)
