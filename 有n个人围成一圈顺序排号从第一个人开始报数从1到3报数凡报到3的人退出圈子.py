n=int(input('输入数字：'))#输入数字
a=list(range(1,n+1))#建立一个列表，存放的是号码数
count=0;#构造一个全局变量，使得其储存每一位报的数
while len(a)>1:#循环直到列表只剩一个元素
	b=a[:]#复制列表，为下一步删除做准备
	for i in range(0,len(b)):#在len(b)的次数中，计数，并去除数
		count+=1
		if count%3==0:#如果报三，则去除a中的这一位
			a.remove(b[i])
print("最后剩下的是序号%d"%a[0])		
