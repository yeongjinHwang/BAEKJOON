t = int(input())
for _ in range(t) :
    num, a = input().split()
    tmp = ''
    for i in a :
        tmp+=int(num)*i
    print(tmp)
