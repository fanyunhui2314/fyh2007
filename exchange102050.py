s=0
for i in range(0,11):
    for j in range(0,6):
        for k in range(0,3):
            if (10*i+20*j+50*k==100):
                s=s+1
                print("i=%d,j=%d,k=%d"%(i,j,k))
                print("第%d种算法:10×%d+20×%d+50×%d=100"%(s,i,j,k))
                print("10元%d张,20元%d张，50元%d张"%(i,j,k))
print("一共有%d种算法"%s)

            
        
