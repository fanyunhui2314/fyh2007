num1,num2,num3=eval(input("请输入三个数值,以英文逗号隔开:"))
if num1>num2 and num1>num3:
   max=num1
elif num2>num1 and num2>num3:
   max=num2
else:
   max=num3
print("三个数中最大数是:",max)
