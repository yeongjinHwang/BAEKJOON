value=[]
for _ in range(5) :
    a = int(input())
    value.append(a)
value=sorted(value)
print(sum(value)//5,value[2],sep='\n')