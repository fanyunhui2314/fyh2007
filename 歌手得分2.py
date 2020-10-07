n=int(input("请输入总共几名评委:"))
score=[ ]
for i in range (n):
    m=input("第%d评委给出的评分是:"%(i+1))
    score.append(eval(m))
score=sorted(score)
max_score = max(score)
min_score = min(score)
lt=score[1:n-1]
score=sum(lt)/len(lt)
print("去掉一个最低分:",min_score)
print("去掉一个最高分:",max_score)
print("该歌手最终成绩为:%.1f"%score)
