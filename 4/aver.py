n = int(input())
aver=0
a=list(map(int,input().split())) 

print(round((sum(a)/len(a)/max(a)*100),6))