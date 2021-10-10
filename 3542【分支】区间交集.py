# 描述
# 输入5个正整数a1、b1、a2、b2和c，如果c在区间[a1, b1]内,
# 并且c也在区间[a2, b2]内输出”in”，否则输出”out”。
# 注意：方括号表示的是闭区间，[a, b]是包括a和b的。

# 输入
# 5个正整数：a1、b1、a2、b2和c，范围在[1, 1000000]，a1 ≤ b1，a2 ≤ b2。

# 输出
# in或out。

a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())
c=int(input())
if c>=a1 and c<=a2 and c>=b1 and c<=b2:
    print("in")
else:
    print("out")