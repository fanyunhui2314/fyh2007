## 统计100以内个位数是2并且能够被3整除的数的个数
sum = 0
for x in range(1,101):
    if x % 3 ==0 and x % 10 ==2:
        sum=sum+1
print("\r")
print("100以内个位数是2并且能够被3整除的数的个数有%d个,它们是:"%sum,end='')
for x in range(1,101):
    if x % 3 ==0 and x % 10 ==2:
        print(x,end='  ')
