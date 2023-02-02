n = int(input())
word=[]
for _ in range(n) :
    i = str(input())
    word.append((len(i),i))
word = sorted(list(set(word)))
for i in range(len(word)) :
    print(word[i][1],end='\n')

