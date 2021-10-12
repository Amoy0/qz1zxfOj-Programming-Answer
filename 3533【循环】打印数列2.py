# 描述
# 打印下面数列的前N项。
# 1  3  7  15  31  63….

# 输入
# 第一行1个整数n，范围在[1,20]。

# 输出
# 一行，N个整数。
n=int(input())
i=0
sum=1
while i<=n-1:
    sum=2**i+sum
    i=i+1
    print(sum-1,end=" ")
