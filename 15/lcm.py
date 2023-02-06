t=int(input())
for _ in range(t) :
    a, b = map(int, input().split())
    tmpA,tmpB=a,b
    while tmpB > 0: tmpA, tmpB = tmpB, tmpA % tmpB
    print(a * b // tmpA)