i=0

for x in range(-114,114):
              for y in range(-114,514):
                            if abs(x-y)+abs(x-2*y)==9:
                                          print(x,y)
                                          i+=1
print(i)
