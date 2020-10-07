def recursion(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
number=int(input("输入一个整数:"))
result=recursion(number)
print("%d的阶乘是:%d"%(number,result))
