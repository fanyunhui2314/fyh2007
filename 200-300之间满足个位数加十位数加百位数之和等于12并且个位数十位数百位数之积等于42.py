for i in range(200,301):
    a=int(i/100)
    b=int((i-100*a)/10)
    c=i-100*a-10*b
    if (a+b+c==12) and (a*b*c==42):
        print("200-300之间满足条件的数是:%d"%(100*a+10*b+c),"\n")
        
        
