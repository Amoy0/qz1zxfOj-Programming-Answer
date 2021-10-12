# 描述
# 打印下面数列的前N项。
# 1  4  10  19  31  46….

# 输入
# 第一行1个整数n，范围在[1,100]。

# 输出
# 一行，N个整数。
n=int(input())
i=0
sum=1
while i<=n-1:
    sum=i*3+sum
    i=i+1
    print(sum,end=" ")
