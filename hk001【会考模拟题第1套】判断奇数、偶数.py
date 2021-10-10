# 描述
# 读入两个整数，判断他们的差，是否为奇数或偶数

# 输入
# 读入两行，每行一个整数

# 输出
# "jishu"或"oushu"
a=int(input())
b=int(input())
c=(a-b)%2
if c==1:
    print("jishu")
else:
    print("oushu")