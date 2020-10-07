for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                m=a*1000+100*b+10*c+d
                n=1000*d+100*c+10*b+a
                if (9*m==n):
                    print("有这样一个四位数，其9倍刚好是其反序数，这个四位数是:%d"%m)
        
