h,m = map(int,input().split())
need = int(input())
cal=need+m
cnt=0
while cal>=60 :
    cnt+=1
    cal=cal-60
h=h+cnt
if h>=24 :
    h=h-24
print(h,cal)
