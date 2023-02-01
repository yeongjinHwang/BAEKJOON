a,max=[],-1
index=[0,0]
for _ in range(9):
    a.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if max<a[i][j] :
            max=a[i][j]
            index[0],index[1]=i+1,j+1
print(max)
print(index[0],index[1])