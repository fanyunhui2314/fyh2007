print("一位数:")
sum1=0
for a in range(1,4):
    print("%d"%a,end='    ')
    sum1=sum1+(a-1)
print("\n")
print("两位数:")
sum2=0
for b in range(1,4):
    for c in range(1,4):
        print("10×%d+%d=%d"%(b,c,10*b+c),end='   ')
        if c==3:
            print("\n")
     
        sum2=sum2+(b-1)*(c-1)
print("\n")
print("三位数:")
sum3=0
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            print("100×%d+10×%d+%d=%d"%(a,b,c,100*a+10*b+c),end='   ')
            if c==3:
                print("\n")
            
            sum3=sum3+(a-1)*(b-1)*(c-1)
print("一位数有%d个数:"%sum1,end='')
for a in range(1,4):
    print("%d"%a,end='  ')
print("\n")
print("两位数有%d个数:"%(sum2),end='')
for b in range(1,4):
    for c in range(1,4):
        print("%d"%(10*b+c),end='   ')
print("\n")        
print("三位数有%d个数:"%(sum3),end='')
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            print("%d"%(100*a+10*b+c),end='   ')
print("\n")
print("一共有%d组合!"%(sum1+sum2+sum3))

            
