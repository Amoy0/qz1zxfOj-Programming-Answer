# Description
# 期末考试成绩出来了，小明同学语文、数学、英语分别考了x、y、z分，请编程帮助小明计算一下，他的总分和平均分分别考了多少分？

# Input
# 三个整数x、y、z分别代表小明三科考试的成绩。

# Output
# 第1行有一个整数，代表总分，第2行有一个小数（保留1位小数）代表平均分。
a,b,h =map(int,input().split())
c=a+b+h
s=c/3
print(c)
print(format(s, '.1f'))