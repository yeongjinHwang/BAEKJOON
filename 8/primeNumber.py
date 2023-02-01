n = int(input())
primeCnt=0
a = map(int,input().split())
for i in a :
    cnt=0
    for k in range(1,i+1) :
        if i%k==0 :
            cnt+=1
    if cnt==2 :
        primeCnt+=1
print(primeCnt)
