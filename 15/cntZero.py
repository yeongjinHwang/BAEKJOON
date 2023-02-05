N, M = map(int, input().split())

def cntZero(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

print(min(cntZero(N,5)-cntZero(M,5)-cntZero(N-M,5), cntZero(N,2)-cntZero(M,2)-cntZero(N-M,2)))