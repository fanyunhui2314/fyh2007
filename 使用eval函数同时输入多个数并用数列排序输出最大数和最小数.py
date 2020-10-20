num1,num2,num3=eval(input("请输入三个数值,以英文逗号隔开:"))
print("num1=%.2f,num2=%.2f,num3=%.2f"%(num1,num2,num3))
x=[]
x.extend([num1,num2,num3])
x.sort()
print("三个数中最大的数是:",x[2])
print("三个数中最小的数是:",x[0])
