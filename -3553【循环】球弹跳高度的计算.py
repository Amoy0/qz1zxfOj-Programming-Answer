n=1
h=float(input())
d=float(10.0)
while n<10:
    d=d+h
    h=h/2
    n=n+1
print(format(5+d, '.4f'))
print(format(h/2,'.7f'))
