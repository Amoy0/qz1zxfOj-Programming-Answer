# 描述
# 输入 4 个整数，求它们之中最小的。

# 输入
# 4个整数，范围在[1,30]。

# 输出
# 只一个整数。
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a<b and a<c and a<d:
    print(a)
if b<a and b<c and b<d:
    print(b)
if c<b and c<a and c<d:
    print(c)
if d<b and d<a and d<c:
    print(d)