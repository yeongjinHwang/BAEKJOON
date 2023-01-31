n = int(input())
tmp=n
cnt=0
while True :
    new = n//10 + n%10
    n = new%10 + n%10*10
    cnt+=1
    if n==tmp :  
        break
print(cnt)
