import sys 
from collections import Counter

t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))
numbers=sorted(numbers)

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod

print(round(sum(numbers)/len(numbers)))
print(numbers[len(numbers)//2])
print(mode(numbers))
print(max(numbers) - min(numbers))