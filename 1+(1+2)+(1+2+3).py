sum=0
n=int(input("输入n的值:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        sum=sum+j
print("sum=",sum)
