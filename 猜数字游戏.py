from  random import*
x=randint(0,9)
for i  in range(10):
    y=eval(input("请输入一个0到9的数:"))
    if x<y:
        print("遗憾，太大了!")
    elif x>y:
        print("遗憾，太小了!")
    else:
        print("预测"+str(i+1)+"次","你猜中了!")
        break
    
