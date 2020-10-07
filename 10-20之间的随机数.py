# 输出10个10-20之间的随机数。
# 使用 random 模块。
print("产生10个10-20之间的随机数!")
import random
for i in range(1,11):
    print("x{}=%6.2f".format(i)%(random.uniform(10,20)))
