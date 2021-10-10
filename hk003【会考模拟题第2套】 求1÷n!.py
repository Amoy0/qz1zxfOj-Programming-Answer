# 描述
# 求"1*1/2*1/3……*1/n"的值
# 必须使用while语句完成，请参考提示，注意输出的格式
# 省略号要半角字符

# 输入
# 读入一个整数n

# 输出
# 输出题面答案

n=int(input())
i=1
sum=float(1)
while i<=n:
    sum=float(sum*(1/i))
    i=i+1
print("1*1/2*1/3......*1/",end="")
print(n,end="")
print("=: ",end="")
print(sum)