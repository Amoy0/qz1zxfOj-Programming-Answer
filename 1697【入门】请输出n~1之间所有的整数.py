# Description
# 从键盘读入一个整数n，请输出n~1之间所有的整数，每行输出1个。
# 比如，假设读入n=5，输出结果如下：
# 5
# 4
# 3
# 2
# 1

# Input
# 一个整数n。

# Output
# 输出n~1之间所有的数，每行1个。
n=int(input())
for i in range (n):
    print(n-i)