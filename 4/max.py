a = []
for _ in range(9):
    b = int(input())
    a.append(b)
print(max(a),a.index(max(a))+1)