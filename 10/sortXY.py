n = int(input())
xy=[]
for _ in range(n) :
    x,y=map(int,input().split())
    xy.append([x,y])
xy=sorted(xy)
for i in range(n) :
    print(xy[i][0],xy[i][1])