import sys
from collections import Counter
n = sys.stdin.readline()
card = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
isCard = list(map(int,sys.stdin.readline().split()))
for i in isCard :
    print(Counter(card)[i],end=' ')