# 描述
# 已知：Sn= 1＋1／2＋1／3＋…＋1／n。显然对于任意一个整数K，当n足够大的时候，Sn大于K。
# 现给出一个整数K（1<=k<=15），要求计算出一个最小的n；使得Sn＞K。

# 输入
# k

# 输出
# n
k=int(input())
sum=0
n=0
while sum<=k:
    n+=1
    sum=sum+1/n
print(n)