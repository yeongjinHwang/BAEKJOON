xNum,yNum,cnt=[],[],0
for _ in range(3) :
    x,y=map(int,input().split())
    xNum.append(x)
    yNum.append(y)
xy=[0,0]
for i in range(3) :
    if xNum.count(xNum[i])==1 :
        xy[0]=xNum[i]
    if yNum.count(yNum[i])==1 :
        xy[1]=yNum[i]
print(xy[0],xy[1])
