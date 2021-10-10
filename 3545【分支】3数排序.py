# 描述
# 输入3个整数a、b和c，按从大到小输出。

# 输入
# 3个正整数：a、b和c，范围在[1,10000]。

# 输出
# 排序后的3个数。

a=int(input())
b=int(input())
c=int(input())
if a>b>c:
    print(a,b,c)
if a>c>b:
    print(a,c,b)
if b>a>c:
    print(b,a,c)
if b>c>a:
    print(b,c,a)
if c>b>a:
    print(c,b,a)
if c>a>b:
    print(c,a,b)