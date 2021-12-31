n=int(input())
a,ap= map(int,input('').split())
b,bp= map(int,input('').split())
c,cp= map(int,input('').split())
an=bn=cn=0
ai=bi=ci=0
while an<n:
              an=an+a
              ai=ai+1
suma=ap*ai 
while bn<n:
              bn=bn+b
              bi=bi+1
sumb=bp*bi 
while cn<n:
              cn=cn+c
              ci=ci+1
sumc=cp*ci  
if suma> sumb:
              min=sumb
else:
              min=suma
if sumc<min:
              min=sumc
print(min)
