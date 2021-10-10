# Description
# 输入一个整数，求出该整数以内的从小到这个整数为止的所有偶数并输出

# Input
# 输入一个整数n

# Output
# 输出只有一行，包含小到n的所有偶数，中间用空格隔开
i=2
n=int(input())
while n>=i:
    print(i,end=' ')
    i=i+2