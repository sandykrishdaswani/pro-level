from itertools import permutations
sandy, krish = map(int, input().split())
x = list(map(int, input().split()))
for i in permutations(x, 2):
    if sum(i) == krish:
        print('yes')
        break
else:
    print('no')
