list1=list(range(1,101))
list2=[ ]
i=1
for i in range(1,101):
    if i%3==0:
        list2.append(list1[i-1])
print("1到100之间能被3整除的数有如下:")
print(list2)
    
