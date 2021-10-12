# Description
# 输入一个正整数k，输出:k  k*k  k*k*k……，当超过8位数时停止。

# Input
# 第一行1个整数k，范围在[2,15]。

# Output
# 一行，多个k的幂。
k=int(input())
result=1
while result < 10000000 :
    result=result*k
    print(result,end=" ")