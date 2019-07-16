bAc=int(input())
sA1=list(map(int,input().split()))
aA1=0
for i in range(bAc):
  for j in range(i,bAc):
    for k in range(j,bAc):
      if(s1[i]<s1[j]<sA1[k]):
        aA1+=1
print(a1)
