# 描述
# 求n个正数的最大数

# 输入
# 第一行一个整数n
# 第二行到n+1行，每行分别一个整数

# 输出
# 输出一个整数，即为所求最大数
n=int(input())
i=1
y=0
while i<=n:
    x=int(input())
    if x>y:
        y=x
    i=i+1
print(y)