s = str(input())
n=[]
for i in range(len(s)) :
    for j in range(i,len(s)):
        n.append(s[i:j+1])
print(len(set(n)))