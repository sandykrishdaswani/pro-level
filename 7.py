as1=int(input())
ss1=0
for j in range(0,as1):
  if(pow(2,j)>as1):
    break
  ss1=as1-pow(2,j)
print(ss1)
