import numpy as np
L=list(open('/var/mobile/201308tq.txt','r'))
s=0
for i in range(len(L)):
     L[i]=int(L[i])
averagetemp=np.mean(L)
print("2013年8月的平均气温是:%5.2f"%averagetemp,"℃")


     
