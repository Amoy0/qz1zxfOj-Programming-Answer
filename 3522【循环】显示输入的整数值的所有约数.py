# Description
# 从键盘输入一个整数，求出并输出该整数的所有约数

# Input
# 输入一个整数n

# Output
# 输出只有一行，包含n的所有约数，中间用空格隔开
num0 = int(input())
num1 = num0
count = 1
count += 1
print("1",end=" ")
num4=0
while count <= num0:
    
    num2 = num1 % count
    num3 = num1 / count
    if num2 == 0:
        num4 =int( num0 / num3)
        print(num4,end=" ")
    count += 1
exit()
