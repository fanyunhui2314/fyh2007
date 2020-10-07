a=int(input("输入第一个数a:"))
b=int(input("输入第二个数b:"))
c=int(input("输入第三个数c:"))
print ("a=%d " %(a),end="   ")
print ("b=%d " %(b),end="   ")
print ("c=%d " %(c))
if (a>b) and (a>c):
    print("max=%d" %(a))
elif (b>a) and (b>c):
    print("max=%d" %(b))
else:
    print("max=%d" %(c))
    

        
