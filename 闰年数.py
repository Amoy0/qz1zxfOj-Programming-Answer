#描述
#输入2 个正整数a和b，表示开始的年份和结束的年份，问从a年到b年有多少闰年？

#输入
#第一行2个整数a和b，范围在[1,  100000]。

#输出
#只一个整数。
a,b= map(int,input('').split())
year=a
i=0
while a<=year<=b:
	if year%4==0 and year%100!=0:
		i=i+1
	elif year%400==0:
		i=i+1
	year=year+1	
print(i)
