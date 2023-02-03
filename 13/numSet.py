n,m = map(int,input().split())
string,isString = set([]),[]
for _ in range(n) :
    string.add(str(input()))
for _ in range(m) :
    isString.append(str(input()))
cnt=0
for i in isString :
    if i in string :
        cnt+=1
print(cnt)