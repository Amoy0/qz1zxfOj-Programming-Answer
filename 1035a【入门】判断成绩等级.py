# 描述
# 输入某学生成绩，如果86分以上(包括86分）则输出“VERY GOOD” ，
# 如果在60到85之间的则输出“GOOD”(包括60和85)，
# 小于60的则输出“BAD”。

# 输入
# 输入只有一行，包括1个整数。

# 输出
# 输出只有一行（这意味着末尾有一个回车符号）。
score=int(input())
if score>=86:
    print("VERY GOOD")
elif score>=60:
    print("GOOD")
else:
    print("BAD")