def draw(n) :
    if n==1 :
        return ['*']
    star = draw(n//3)
    tmp=[]
    for i in star :
        tmp.append(i*3)
    for i in star :
        tmp.append(i+' '*(n//3)+i)
    for i in star :
        tmp.append(i*3)
    return tmp

n = int(input())
star = draw(n)
for i in range(len(star)) :
    print(star[i])