sandy, m = [int(i) for i in input().split()]
uma = []
Lis = [int(i) for i in input().split()]
for _ in range(m):
    l, k = [int(i) for i in input().split()]
    uma.append(min(Lis[l-1:k]))
for i in uma:
    print(i)
