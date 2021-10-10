# 描述
# 输入某学生成绩，如果90分以上(包括90分）则输出“A” ，如果在80到89之间的则输出“B”(包括80和89)，如果在60到79之间的则输出“C”(包括60和79)，小于60的则输出“D”。

# 输入
# 输入只有一行，包括1个整数。

# 输出
# 输出只有一行。

score=int(input())
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=60:
    print("C")
else:
    print("D")
