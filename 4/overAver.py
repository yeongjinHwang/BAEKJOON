c = int(input())
for _ in range(c) :
    a = list(map(int,input().split()))
    aver = sum(a[1:]) / a[0]
    cnt = 0
    for i in a[1:] :
        if aver < i :
            cnt+=1
    print(f'{cnt/a[0]*100:.3f}%')