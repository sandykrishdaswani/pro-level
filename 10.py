sandy=int(input())
nee=list(map(int,input().split()))
eee=0
for s in range(0,sandy):
	for v in range(0,s):
		if nee[v]<nee[s]:
			eee=eee+nee[v]
print(eee)
