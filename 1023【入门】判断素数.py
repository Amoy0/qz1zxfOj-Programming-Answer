# 描述
# 任意输入一个整数，判断它是否为素数。是的话输出"T",不是的话输出"F"
# 质数（prime number）又称素数，质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。

# 输入
# 输入只有一行，包括1个整数。

# 输出
# 输出只有一行。
n=int(input())
bool=0
for i in range(2,n):
    if n%i==0:
        bool=1
        break
if bool or n<=1:
    print("F")
else:
    print("T")