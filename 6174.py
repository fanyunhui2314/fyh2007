num = int(input("请输入一个四位整数:"))
c = num
while c != 6174:
    digits = list(str(c))
    digits.sort(reverse=True) #排列出最大数
    if len(digits) < 4:
        digits.append('0')
    a = int(''.join(digits))       #把列表里的元素合并成一个四位整数
    digits.reverse()                 #排列出最小数
    b = int(''.join(digits))
    c = a - b
    print("%d - %d = %d" % (a, b, c))
