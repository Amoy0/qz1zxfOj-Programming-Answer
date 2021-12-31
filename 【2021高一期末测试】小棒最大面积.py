l=int(input())
l=int(l/2)
s=0
s1=0
for a in range(1,l):
              s=a*(l-a)
              if s>s1:
                            s1=s
print(s1)
