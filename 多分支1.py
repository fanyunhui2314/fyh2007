active=True
while active:
    score=int(input('输入一个成绩(0-100之间)(输入-1退出程序):'))
    if score==-1:
        active=False
    else:
        if 90<=score<=100:
            print('等级是A')
        else:
            if 80<=score<90:
                print('等级是B')
            else:
                if 70<=score<80:
                    print('等级是C')
                else:
                    if 60<=score<70:
                        print('等级是D')
                    else:
                        if 0<=score<60:
                            print('等级是E')
                        else:
                            print('输入错误,请重新输入！')
                            continue
                    
                        
                    
                    
                    
                        
                    
                    
