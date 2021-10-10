# Description
# 输入3个正整数a、b和c，如果c在区间[a, b]内输出”in”，否则输出”out”。
# 注意：方括号表示的是闭区间，[a, b]是包括a和b的。

# Input
# 3个正整数：a、b和c，范围在[1, 1000000]，a ≤ b。

# Output
# in或out。
a=int(input())
b=int(input())
c=int(input())
if c>=a and c<=b:
    print("in")
else:
    print("out")