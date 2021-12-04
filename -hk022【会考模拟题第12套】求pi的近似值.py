# 描述
# 必须使用while语句完成，请参考提示，注意输出的格式

# 输入
# null

# 输出
# pi的近似值（输出20位浮点型数值）
sum,a,b,t=0.0,1,1.0,1.0
while 1:
    sum=sum+t
    a=-a
    b+=2
    t=a/b
    pi=sum*4
    print(b,"pi的值是{:.100f}".format(pi))