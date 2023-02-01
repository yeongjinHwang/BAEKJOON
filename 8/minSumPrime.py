m = int(input())
n = int(input())
primeNum=[]
for i in range(m,n+1) :
    cnt=0
    for k in range(1,i+1) :
        if i%k==0:
            cnt+=1
    if cnt==2 :
        primeNum.append(i)
if(len(primeNum)):
    print(sum(primeNum),min(primeNum),sep='\n')
else :
    print(-1)