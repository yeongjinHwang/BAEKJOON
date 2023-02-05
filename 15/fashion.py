t = int(input())
for _ in range(t) :
    tmp,cnt={},1
    n = int(input())
    for _ in range(n) :
        a= list(map(str,input().split()))
        if not a[1] in tmp :
            tmp[a[1]]=1
        else :
            tmp[a[1]]+=1
    for i in tmp :
        cnt*=tmp[i]+1
    print(cnt-1)