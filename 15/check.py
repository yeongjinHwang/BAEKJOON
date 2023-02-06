import sys

def gcd(a, b):
    while b > 0: a, b = b, a%b
    return a

n = int(sys.stdin.readline())
numList = list()
for _ in range(n):
    numList.append(int(sys.stdin.readline()))
numList.sort()
nowGcd = numList[1] - numList[0]
for i in range(1, n-1):
    nowGcd = gcd(nowGcd, numList[i+1]-numList[i])

yaksu = [nowGcd]
for i in range(2, int(nowGcd**0.5)+1):
    if nowGcd%i == 0:
        yaksu.append(i)
        yaksu.append(nowGcd//i)
yaksu=sorted(list(set(yaksu)))
for i in yaksu :
    print(i,end=' ')