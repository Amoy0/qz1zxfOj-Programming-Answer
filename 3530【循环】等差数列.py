# Description
# 一列数，如果相邻2个的差都相等，就叫等差数列。例如：2,5,8,11,14….。
# 现在给定开始数a和差d，输出第n项。一行3个正整数：a、d和n，范围在[-100,100]。

# Input
# 一行3个正整数：a、d和n，范围在[-100,100]。

# Output
# 3行n个整数。
a=int(input())
d=int(input())
n=int(input())
r=a+d*(n-1)
print(r)