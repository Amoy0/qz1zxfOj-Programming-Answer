# Description
# 输入3个整数a、b和c，输出其中的最大值。

# Input
# 3个正整数：a、b和c，范围在[1,10000]。

# Output
# 一个正整数。
a=int(input())
b=int(input())
c=int(input())
if a>b>c or a>c>b:
    print(a)
if b>a>c or b>c>a:
    print(b)
if c>b>a or c>a>b:
    print(c)
