import sys
n = int(input())
num = []
for _ in range(n) :
    num.append(int(sys.stdin.readline()))
num=sorted(num)
for i in range(n) :
    print(num[i])
