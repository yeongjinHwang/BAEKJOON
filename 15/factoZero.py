import math
n = int(input())
fac = str(math.factorial(n))
cnt=0
for i in range(-1,-len(fac),-1) :
    if fac[i]=='0' : cnt+=1
    else : break
print(cnt)