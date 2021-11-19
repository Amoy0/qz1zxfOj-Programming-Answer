# 描述
# 输入一个整数，连续显示出该整数个*(使用 for 语句) 题目重复

# 输入
# 输入一个正整数n

# 输出
# 输出一行，包含n个“*”

n=int(input())
for i in range(n):
  print("*",end="")
