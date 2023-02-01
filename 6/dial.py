s = str(input())

def stoi(a) :
    if a>='A' and a<='O' :
        num = (ord(a) - 65) // 3 +2
    elif a>='P' and a<='S' :
        num = 7
    elif a>='T' and a<='V' :
        num = 8
    elif a>='W' and a<='Z' :
        num = 9
    return int(num+1)
sec = 0
for i in s :
    sec += stoi(i)
print(sec)