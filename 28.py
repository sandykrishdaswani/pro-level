sandy=int(input())
mom=list(map(int,input().split()))
mom.sort()
sin=0
san=0
for i in range(len(mom)):
    if mom[i]>=sin:
        sa=san+1
    sin=sin+mo[i]
print(san)
