s=0
s1=[0]
list1=[]
for i in range(1,8):
     s=s+2**(i-1)
     list1.append([2**(i-1)])
for i in range(1,8):
     print("list1[{}]".format(i-1),"=",2**(i-1))
for i in range(1,8):
    s1=str(s1)+'+'+str(list1[i-1])
print(s1,"=",s,end='')   
    
