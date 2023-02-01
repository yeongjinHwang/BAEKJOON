n = int(input())

for _ in range(n):
    a = list(input())
    cnt,sum = 0, 0  
    for ox in a:
        if ox == 'O':
            cnt += 1  
            sum += cnt  
        else:
            cnt = 0
    print(sum)