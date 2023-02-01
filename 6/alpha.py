n = str(input())
index=[]
for _ in range(26):
    index.append(-1)
for i in n :
    index[ord(i)-97] = n.index(i)
for i in index :
    print(i,end=' ')

