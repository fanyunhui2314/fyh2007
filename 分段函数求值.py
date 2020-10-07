"""
分段函数求值
	3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
	5x + 3	(x < -1)
Version: 0.1
"""
x = float(input("输入x="))
if x>1:
    y = 3*x-5
    print("x=%.2f"%x)
    print("y=3x-5")
    print("y=%.2f"%y)
elif x>=-1:
    y=x+2
    print("x=%.2f"%x)
    print("y=x+2")
    print("y=%.2f"%y)
else:
    y=5*x+3
    print("x=%.2f"%x)
    print("y=5x+3")
    print("y=%.2f"%y)
