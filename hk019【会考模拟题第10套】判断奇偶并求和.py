# 描述
# 获得用户输入的一个整数n，如果n是偶数，求2+4+···+n的值，如果n是奇数，求1+3+···+n的值。
# 必须使用while语句完成，请参考提示，注意输出的格式

# 输入
# 输入一个整数n

# 输出
# 奇数和或者偶数和。
n=int(input())
s=int(0)
i=int()
if n%2==0:
    i=0
    while i<=n:
        s=s+i
        i+=2
    print(s)
else:
    i=1
    while i<=n:
        s=s+i
        i+=2
    print(s)