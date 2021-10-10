# 描述
# 输入规定个数个整数并显示出它们的合计值和平均值

# 输入
# 输入为n+1行，第一行为整数n
# 第2~n+1行为n个整数

# 输出
# 输出为两行，第一行为n个整数的总和
# 第二行为n个整数平均值，其中平均值保留两位小数
n=int(input())
sum=0
i=1
while i<=n:
    a=int(input())
    sum=sum+a
    i=i+1
print('sum=',sum)
average=sum/n
print('average=',end='')
print("%.2f" % average)