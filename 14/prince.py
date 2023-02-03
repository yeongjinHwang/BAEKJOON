import math
t = int(input())
for _ in range(t) :
    x1,y1,x2,y2 = map(int,input().split())
    n=int(input())
    cnt=0
    for _ in range(n) :
        cx,cy,r = map(int,input().split())
        a=math.sqrt((x1-cx)**2+(y1-cy)**2)
        b=math.sqrt((x2-cx)**2+(y2-cy)**2)
        if r>a and r>b :
            pass
        elif r>a or r>b :
            cnt+=1
    print(cnt)

