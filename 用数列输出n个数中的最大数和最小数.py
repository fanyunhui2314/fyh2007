n=int(input("输入数的个数:"))
x=[]
for i in range(0,n):
   temp=int(input("输入第%d个数:"%(i+1)))
   x.append(temp)
x.sort()
max=x[n-1]
min=x[0]
for i in range(0,n):
  print("x[%d]=%d"%(i,x[i]),end='  ')
print("\r")
print("%d个数中最大数是%d,%d个数中最小数是%d"%(n,max,n,min))

              
