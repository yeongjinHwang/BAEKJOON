a, b = map(int, input().split())
tmpA,tmpB=a,b
while tmpB > 0: tmpA, tmpB = tmpB, tmpA % tmpB
print(tmpA, a * b // tmpA,sep='\n')
