def d(n) :
    if n<10 :
        n=2*n
    elif n<100 :
        n = n//10 + n%10 + n
    elif n<1000 :
        n = n//100 + (n%100)//10 + n%10 + n
    elif n<10000 :
        n = n//1000 + (n%1000)//100 + (n%100)//10 + n%10 + n
    return n

selfNum, remover = [], []
for i in  range(1,10001) :
    selfNum.append(i)
    if d(i)<=10000 :
        remover.append(d(i))
remover = set(remover)
for i in remover :
    selfNum.remove(i)
for i in selfNum :
    print(i)