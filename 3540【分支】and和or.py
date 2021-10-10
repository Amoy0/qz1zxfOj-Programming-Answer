# 描述
# 输入2个正整数a和b。如果a和b都是偶数，或者a和b都是3的倍数，就输出’1’；否则输出’0’。

# 输入
# 2个正整数：a和b，范围在[1,100]。

# 输出
# 一行，1或0。
a=int(input())
b=int(input())
c=a%2+b%2
d=a%3+b%3
if c==0 or d==0:
    print("1")
else:
    print("0")