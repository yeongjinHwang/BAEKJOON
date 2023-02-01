n = int(input())
line = 1
while True:
    if n<=sum(range(1,line+1)):
        break
    line+=1
k = n-sum(range(1,line))
if line % 2==0: 
    a = k 
    b = line+1-a
else: 
    a = line+1-k
    b = k 
print(a,'/',b,sep='')