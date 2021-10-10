# 描述
# 获得用户输入的分钟数，换算成小时分钟表示，并输出结果

# 输入
# 一个数，代表分钟数

# 输出
# 换算后的时间，用小时分钟表示
min=int(input())
hour=min//60
min2=min-hour*60
print(hour," ",min2)