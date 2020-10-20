num1,num2,num3=eval(input("请输入三个数值,以英文逗号隔开:"))
print("num1=%.2f,num2=%.2f,num3=%.2f"%(num1,num2,num3))
max=num1
min=num1
if num2>max:
   max=num2
if num3>max:
   max=num3
print("三个数中最大的数是:",max)
if num2<min:
   min=num2
if num3<min:
   min=num3
print("三个数中最小的数是:",min)
