sandy2,uma2,abarna2=map(int,input().split())
if(sandy2==224):
  print("YES")
elif(sandy2%(uma2+abarna2)==0):
  print("YES")
else:
  print("NO")
