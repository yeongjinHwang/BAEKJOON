def hansu(n) :
    cnt = 0
    if n <= 99 :
        for _ in range(n):
            cnt+=1
    elif n<=110 :
        cnt=99
    else :
        cnt=99
        for i in range(110,n+1) :
            hun,ten,one = i//100, (i%100)//10 ,i%10
            if hun+one == 2*ten :
                cnt+=1
    return cnt

n = int(input())
print(hansu(n))