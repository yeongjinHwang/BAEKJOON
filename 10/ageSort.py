n = int(input())
info=[]
for i in range(n) :
    age,name = map(str,input().split())
    info.append([int(age),name])
info=sorted(info,key=lambda x : x[0])
for i in range(n) :
    print(info[i][0],info[i][1])