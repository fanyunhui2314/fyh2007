s=0
a=list(range(1,101))
for i in range(0,100):
    print("a[%d]=%d"%(i,i+1),end=' ')
    if i>0 and i%10==0:
        print("\r")
    s=s+a[i]
print("\n s=",s)
