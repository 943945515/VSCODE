i = int(input('利润: '))
lirun = [1000000,600000,400000,200000,100000,0]
tichenlv = [0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for x in range(0,6):
    if i>lirun[x]:
        r+=(i-lirun[x])*tichenlv[x]
        print((i-lirun[x])*tichenlv[x])
        i=lirun[x]
print(r)