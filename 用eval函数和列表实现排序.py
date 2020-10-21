x=[]
num1,num2,num3,num4,num5,num6,num7,num8,num9,num10=eval(input("输入10个数,用英文逗号隔开:"))
x.extend([num1,num2,num3,num4,num5,num6,num7,num8,num9,num10])
for i in range(0,10):
    for j in range(i+1,10):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
for i in range(0,10):
    print(x[i],end='  ')

    
