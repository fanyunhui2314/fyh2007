# 公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱
# 用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，
# 问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱
print("百文买百鸡问题所有可能的解如下:")
for i in range(0,100):
        for j in range(0,100):
                for k in range(0,100):
                        if (5*i+3*j+k/3==100) and (k%3==0) and (i+j+k==100):
                                print("公鸡%d只,%d*5=%d文"%(i,i,5*i),end=' ')
                                print("母鸡%d只,%d*3=%d文"%(j,j,3*j),end=' ')
                                print("小鸡%d只,%d*1/3=%d文"%(k,k,int(k/3)),end=' ')
                                print("\n")
                                
                                
 
