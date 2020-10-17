## 编程实现判断这个人的身材是否正常!
## (公式: 体重(kg)/身高(m)的平方值 在18.5 ~ 24.9之间属于正常
height =float(input("请输入一个人的身高(m):"))
weight =float(input("请输入一个人的体重(kg):"))
x = weight / (height ** 2)
if 18.5 < x < 24.9:
    print("此人身材正常!")
else:
    print("此人身材不正常!")
