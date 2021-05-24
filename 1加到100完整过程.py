print("-"*21)
s=0
for i in range(1,101):
    print("当s=%d,i=%d时"%(s,i))
    s=s+i
    print("s=%d+%d=%d"%(s-i,i,s))
    print("-"*21)
