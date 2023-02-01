a=[]
for _ in range(10):
    b = int(input())
    a.append(b%42)
a = set(a)
print(len(a))