a,b,c = map(int,input().split())
if a==b and b==c :
    print(10000+a*1000)
elif a==b or b==c or a==c :
    if a==b or a==c :
        print(a*100+1000)
    else :
        print(b*100+1000)
else :
    print(max(a,b,c)*100)