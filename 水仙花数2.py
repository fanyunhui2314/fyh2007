print("水仙花数:")
for a in range(1,10):
        for b in range(0,10):
                for c in range(0,10):
                        if (100*a+10*b+c==a**3+b**3+c**3):
                           print("%d^3+%d^3+%d^3=%d"%(a,b,c,100*a+10*b+c))     
                           
