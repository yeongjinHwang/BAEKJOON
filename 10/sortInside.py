n = str(input())
m = []
for i in range(len(n)) :
    m.append(ord(n[i])-48)
m=list(reversed(sorted(m)))
for i in m :
    print(i,end='')