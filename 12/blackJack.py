from itertools import combinations
n,m = map(int,input().split())
num = list(map(int,input().split()))
near=0
for i in combinations(num,3):
    tmp = sum(i)
    if near < tmp <= m :
        near = tmp
print(near)
