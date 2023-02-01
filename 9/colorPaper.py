k=[[0]*100 for _ in range(100)]
n = int(input())
for _ in range(n) :
    a, b = map(int,input().split())
    for i in range(a,a+10) :
        for j in range(b,b+10) :
            k[i][j]=1
cnt = 0
for i in range(100) :
    cnt+=k[i].count(1)
print(cnt)