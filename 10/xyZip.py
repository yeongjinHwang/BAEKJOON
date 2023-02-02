n = int(input())
x = list(map(int,input().split()))
sortX = sorted(set(x))
dic = {sortX[i]: i for i in range(len(sortX)) }
for i in x :
    print(dic[i],end=' ')