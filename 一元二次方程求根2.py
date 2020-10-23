from math import *
a=float(input("请输入a的值:"))
b=float(input("请输入b的值:"))
c=float(input("请输入c的值:"))
if a!=0:
    delta=b**2-4*a*c
    if delta<0:
        print("无实根!")
    elif delta==0:
        s=-b/(2*a)
        print("唯一根x=%d"%s)
    else:
        root=sqrt(delta)
        root1=(-b+root)/(2*a)
        root2=(-b-root)/(2*a)
        print("root1=",root1,"\t","root2=",root2)
else:
    print("%dx+%d不是一元二次方程!"%(b,c))
