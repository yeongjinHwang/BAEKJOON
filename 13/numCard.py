import sys
n = sys.stdin.readline()
card = set(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
isCard = list(map(int,sys.stdin.readline().split()))
for i in isCard :
    if i not in card :
        print('0',end=' ')
    else :
        print('1',end=' ')