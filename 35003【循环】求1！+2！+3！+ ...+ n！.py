#描述
#输入一个正整数n 求1！+2！+3！ ... + n！

#输入
#输入一行，包含一个正整数n。

#输出
#输出一行，包含一个正整数，表示答案
n=int(input())
sum1=1
sum=0
for i in range(1,n+1):
              a=1
              sum1=1
              while a<=i:
                            sum1=sum1*a
                            a=a+1
              sum=sum+sum1
print(sum)
