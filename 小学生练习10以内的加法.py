import random
s = int(input('输入题目数量:'))
ture=0
for i in range(0,s):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print('%d+%d=?' %(num1,num2))
    sum = num1 + num2
    student = int(input('请输入答案:'))
    if student==sum:
        print('答案正确!')
        ture += 1
    else:
        print('答案错误,正确的答案是:%d'%sum)
print('ture:%d'%(ture))
zql = (ture/s)*100
print('学生答题总数为:%d\n 正确数量为:%d\n 正确率为:%.2f%%'%(s,ture,zql))
