a=int(input("输入第一季度节水吨数(>50):"))
b=float(input("输入每个季度的节水增长率(0-1之间):"))
fourseason=a*((1+b)**3)
print("学校希望第四季度能够节约用水的数量是"+str(fourseason)+"吨")