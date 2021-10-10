# 描述
# 输入3个不同的整数a、b和c，输出中间大小的数。

# 输入
# 3个正整数：a、b和c，范围在[1,10000]。

# 输出
# 输出中间大小的数
a=int(input())
b=int(input())
c=int(input())
if a<b<c:
    print(b)
if a<c<b:
    print(c)
if b<a<c:
    print(a)
if b<c<a:
    print(c)
if c<b<a:
    print(b)
if c<a<b:
    print(a)