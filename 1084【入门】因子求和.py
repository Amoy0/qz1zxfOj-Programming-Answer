# 描述
# 已知一个正整数N（20 <= N <= 800000000），请你编写程序求出该数的全部因子（不包括1和n）的和。

# 输入
# 一个正整数n。

# 输出
# 一个整数代表n的因子和。
n=int(input())
m=n
sum=1
if n<=3:
    print(0)
else:
    for i in range(2,n):
        if i*i>m and n!=m: 
            sum=sum-1-m
            break
        if i*i>m and n==m:
            sum=0
            break
        if n%i==0:
            total=0
            x=-1
            while n%i==0:
                n=n/i
                x=x+1
            for y in range(0,x+2):
                total=total+(i**y)
            sum=sum*total
    print(sum)