## 输入任意一个正整数，求它是几位数
sum=0
x = int(input("请输入一个正整数:"))
y=x
while x != 0:
        sum=sum+1
        x = x // 10
print("%d是%d位数!"%(y,sum))
