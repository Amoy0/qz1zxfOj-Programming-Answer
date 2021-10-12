# 描述
# 求下列双等差数列的第N项。
# 1 2 4 7 11 16 22…

# 输入
# 一行1个正整数：N，范围在[1,100]。

# 输出
# 1个整数。
n=int(input())
i=0
x=1
sum=1
while i<=n-1:
    sum=i+sum
    i=i+1
print(sum)