a=list(range(1,101))
zuidashu=a[0]
for i in range(1,100):
    if a[i]>zuidashu:
        zuidashu=a[i]
print(a)        
print("数列中最大数是:%d"%zuidashu)
zuixiaoshu=a[0]
for i in range(1,100):
    if a[i]<zuixiaoshu:
        zuixiaoshu=a[i]
print("数列中最小数是:%d"%zuixiaoshu)




