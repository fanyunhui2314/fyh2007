"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
"""

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a:
    print("三角形周长:%.2f"%(a+b+c))
    p = (a+b+c)/2
    area =(p*(p-a)*(p-b)*(p-c))**0.5
    print("三角形面积:%.2f"%(area))
else:
    print("不能构成三角形")
