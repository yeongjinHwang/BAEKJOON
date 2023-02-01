n = list(map(int,input().split()))
a,b =[],[]
for j in range(n[0]):
    a.append(list(map(int,input().split())))
for j in range(n[0]):
    b.append(list(map(int,input().split())))

for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j]+=b[i][j]
        print(a[i][j],end=' ')
    print('')
        