n = int(input())
sort=[]
for _ in range(n) :
    a = int(input())
    sort.append(a)
sort=sorted(sort)
for i in range(n) :
    print(sort[i])