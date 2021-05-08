n=int(input("请输入学生人数:"))
i=1
max=0
while i<=n:
	score=int(input("请输入第%d个学生成绩"%i))
	if score>max:
		max=score
	i=i+1
print("成绩最好的是"+str(max))
