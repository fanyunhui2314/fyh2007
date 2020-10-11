sum=0
for i  in range(1,100):
    if i%2==1:
        sum=sum+i
    else:
        sum=sum-i
print("1-2+3-4+5-6+......+99=%d"%sum)
