n = int(input())
three,five=0,0
while n>0 :
    if n%5==0 :
        five = n//5
        n=n-five*5
    else :
        three+=1
        n-=3
if n!=0 :
    print(-1)
else :
    print(three+five)