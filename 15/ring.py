from fractions import Fraction
n = int(input())
ring = list(map(int,input().split()))
for i in range(1,n) :
    a = Fraction(ring[0],ring[i])
    print(f'{a.numerator}/{a.denominator}')
