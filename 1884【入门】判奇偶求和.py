# 描述
# 输入一个正整数n,如果n是奇数,则求1-n之间所有的偶数之和；如果n是偶数,则求n所有的约数之和(包括1和本身)。

# 输入
# 一行，一个整数n（0<n<3010)

# 输出
# 一行，一个整数。
n=int(input())
sum=0
if n%2==1:
  for i in range (2,n+1,2):
    sum=sum+i
else:
    num1 = num0 =n
    count = 2
    num4=0
    while count <= num0: 
        num2 = num1 % count
        num3 = num1 / count
        # print(sum,num4,int(num0/num3))
        if num2 == 0 and num4!=int(num0/num3):
            num4 =int( num0 / num3)
            sum=sum+num4
        count += 1
    sum=sum+1
print(sum)