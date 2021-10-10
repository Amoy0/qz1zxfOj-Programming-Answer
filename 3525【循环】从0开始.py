# Description
# C语言编程中，数数喜欢从0开始。比如数数5次为: 0,1,2,3,4，其中的妙处只有高级的C程序员知道。
# 现在输入n，要你按照C程序员的方式数数。

# Input
# 一行1个正整数：n，范围在[1,1000]。

# Output
# 一行n个整数：0 1 2…。
n=int(input())
i=0
while i<n:
    print(i,end=' ')
    i=i+1