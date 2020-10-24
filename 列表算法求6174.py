###给定任一个各位数字不完全相同的四位正整数，把四个数字按照非递增顺序排序
##再按照非递减排序，然后用第一个数字减去第二个数字，将得到一个新数字。
###一直重复这样的操作，变回达到停在有‘数字黑洞的’6174，这个神奇的数字叫卡普耶卡(D.R.Kaprekar)常数
print ("满足条件的四位数是:",end='')
for i in range(1000,10000):
    a=int(i/1000)
    b= int((i - 1000*a)/100)
    c= int((i - 1000*a-100*b)/10)
    d= i - 1000*a-100*b-10*c
    x=str(1000*a+100*b+10*c+d)
    digits=list(x)
    digits.sort(reverse=True) #排列出最大数
    s1= int(''.join(digits))       #把列表里的元素合并成一个四位整数
    digits.reverse()                 #排列出最小数
    s2=int(''.join(digits))
    if s1-s2==i:
        print("%d-%d=%d"%(s1,s2,i))
     
    
