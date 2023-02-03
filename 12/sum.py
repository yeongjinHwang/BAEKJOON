n = int(input())
result=0
for i in range(n+1) :
    a = list(map(int,str(i)))
    b = i + sum(a)
    if b == n :
        result=i
        break
print(result)