n = int(input())
six,cnt=[],666
while True :
    i = str(cnt)
    if '666' in i :
        six.append(i)
    if len(six)==n :
        print(six[-1])
        break
    else : 
        cnt+=1