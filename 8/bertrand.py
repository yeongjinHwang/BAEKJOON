n = 123456
prime = [1] * (2*n+1)
prime[0], prime[1] = 0,0

for i in range(2, int((2*n)**0.5)+1):
    if prime[i]:
        j = 2
        while (i*j) <= (2*n):
            prime[i*j] = 0
            j += 1

while True :
    k = int(input())
    if not k :
        break
    print(prime[k+1:(2*k)+1].count(1))