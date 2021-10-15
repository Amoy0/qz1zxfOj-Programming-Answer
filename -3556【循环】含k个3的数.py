m,k=map(int,input().split())
if m%19==0:
    i=1
    z=0
    while i*10<=m:
        i=i*10
    while i>=1:
        x=int(m//i)
        m=m-i*x
        i=i/10
        if x==3:
            z=z+1
    if z==k:
        print("YES")
    else:
        print("NO")
else:
    print("NO")