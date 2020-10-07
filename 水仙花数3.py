print("水仙花数:",end='  ')
for i in range(100,1000):
    s=list(str(i))
    hun=int(s[0])
    ten=int(s[1])
    one=int(s[2])
    if i == one**3+ten**3+hun**3:
        print(i,end='       ')
