sandy,mes=input().split()
san=abs(len(mes)-len(sandy))
for y in range(len(sandy)):
  if(len(mes)==1 and mes[y] in sandy):
    break
  if(sandy[y]!=mes[y]):
    san=san+1
print(san)    
