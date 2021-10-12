# 描述
# 打印下面数列的前N项。
# 10 9 7 4 0 -5….

# 输入
# 第一行1个整数n，范围在[1,100]。

# 输出
# 一行，N个整数。
n=int(input())
i=0
sum=10
while i<=n-1:
    sum=sum-i
    i=i+1
    print(sum,end=" ")
    
