n,k=map(int,input().split())
nFac,nMinusKFac,kFac=1,1,1
if k<0:
    print(0)
elif 0<=k<=n :
    for i in range(1,n+1) :
        nFac*=i
    for i in range(1,n-k+1) :
        nMinusKFac*=i
    for i in range(1,k+1) :
        kFac*=i
    print(int(nFac/(kFac)/(nMinusKFac)))
else :
    print(0)