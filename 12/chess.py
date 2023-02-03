import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
cnt = []
for i in range(n - 7):
    for j in range(m - 7):
        w,b=0,0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (l + k) % 2 == 0:
                    if graph[k][l] != 'W': w += 1
                    else: b += 1
                else:
                    if graph[k][l] != 'B': w += 1
                    else: b += 1
        cnt.append(w)
        cnt.append(b)
print(min(cnt))