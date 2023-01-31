price, num = int(input()), int(input())
tmp = 0
for _ in range(num):
    a, b = map(int, input().split())
    tmp = tmp+a*b
if tmp==price :
    print('Yes')
else :
    print('No')