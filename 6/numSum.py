n = int(input())
a = str(input())
b=[]
for i in a :
    b.append(ord(i)-48)
print(sum(b))