t = int(input())
for _ in range(t) :
    a = list(map(int,input().split()))
    xx=a[2]//a[0]+1
    yy=a[2]%a[0] *100
    if a[2]%a[0]==0 :
        xx=a[2]//a[0]
        yy=a[0]*100
    print(yy+xx)