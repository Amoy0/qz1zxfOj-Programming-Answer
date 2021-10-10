# 描述
# 判断三角形是否存在

# 输入
# 三行，每行一个整数表示一条边

# 输出
# “yes”
# “no”
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print("yes")
else:
    print("no")