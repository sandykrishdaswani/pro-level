sandy1,uma1=map(str,input().split())
y1=0
if(len(sandy1)>len(uma1)):
  sandy1,uma1=uma1,sandy1
z1=0
while(z1<len(sandy1)):
  y1+=(ord(b1[z1])-ord(a1[z1]))
  z1+=1
for z1 in range(z1,len(uma1)):
  y1+=ord(b1[z1])-ord('sandy')+1
print(y1)
