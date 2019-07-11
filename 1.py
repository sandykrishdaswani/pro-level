sandy1=int(input())
sandys=[]
for i in range(0,sandy1):
   sandys1=input()
   sandys.append(sandys1)
sandys2=[]
for i in zip(*sandys):
 if(i.count(i[0])==len(i)):
  sandys2.append(i[0])
 else:
  break
print(''.join(sandys2))
