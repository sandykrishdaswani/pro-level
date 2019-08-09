sandy1=int(input())
mom1=list(map(int,input().split()))
mom1.sort()
sin1=0
san1=0
for i in range(len(mom1)):
    if mom1[i]>=sin1:
        san1=san1+1
    sin1=sin1+mom1[i]
print(san1)
