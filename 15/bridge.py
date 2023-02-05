T = int(input())

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num = num*i
    return num

for i in range(T):
    N, M = map(int, input().split())
    num = factorial(M) // (factorial(N) * factorial(M - N))
    print(num)