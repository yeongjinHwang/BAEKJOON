n,m = map(int,input().split())
noListen,noSee=set([]),set([])
cnt=0
both=set([])
for _ in range(n) :
    noListen.add(str(input()))
for _ in range(m) :
    noSee.add(str(input()))
for i in noListen :
    if i in noSee :
        cnt+=1
        both.add(i)
print(cnt)
both=sorted(both)
for i in both :
    print(i)
