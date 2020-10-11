## 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为
from sys import stdout
filename = input('输入文件名:')
fp = open(filename,"w")
ch = input('输入字符串:')
while ch != '#':
    fp.write(ch)
    stdout.write(ch)
    print("\r")
    ch = input("")
fp.close()
