mom=int(input())
non=list(map(int,input().split()))
of=[]
pr=1
for i in non:
  if i not in of:
    of.append(i)
for i in range(len(of)-1):
  if (of[i]<o[i+1]):
    pr+=1
print(pr)
