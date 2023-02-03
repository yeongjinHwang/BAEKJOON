n = int(input())
total=[]
for _ in range(n) :
    x,y = map(int,input().split())
    total.append([x,y])
for i in total : 
    tmp = 1
    for j in total :
        if i[0]<j[0] and i[1]<j[1] :
            tmp+=1
    print(tmp,end=' ')