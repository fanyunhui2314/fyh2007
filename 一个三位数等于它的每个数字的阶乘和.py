for x  in range(100,1000):
    i=int(x/100)
    p1=1
    for a in range(1,i+1):
        p1=p1*a
    j=int((x-100*i)/10)
    p2=1
    for b in range(1,j+1):
        p2=p2*b
    k=x-100*i-10*j
    p3=1
    for c in range(1,k+1):
        p3=p3*c
    if (100*i+10*j+k)==(p1+p2+p3):
        print("有这样一个三位数，该三位数等于每个数字的阶乘和，这个数是:%d"%(100*i+10*j+k))

    
