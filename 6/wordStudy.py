s = str(input().upper())
tmp = list(set(s))
cnt=[]
for i in tmp :
    cnt.append(s.count(i))
if cnt.count(max(cnt)) > 1:
    print('?')
else :
    print(tmp[cnt.index(max(cnt))])