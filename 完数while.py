a=[]
i=2
while i<=1000:
   s=i
   j=1
   while j<i:
      if i%j==0:
         s=s-j
      j=j+1
   if s==0:
      a.append(i)
   i=i+1
print(a)

