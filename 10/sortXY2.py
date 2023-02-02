n = int(input())
xy=[]
for _ in range(n) :
    x,y=map(int,input().split())
    xy.append([y,x])
xy=sorted(xy)
for i in range(n) :
    print(xy[i][1],xy[i][0])