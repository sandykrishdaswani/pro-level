sandy1=input()
car=0
for i in range(0,len(sandy1)):
    sas=sandy1[0:i]+sandy1[i+1::]
    if int(sas)%8==0:
        car=1
        break
if car==1:
    print("yes")
else:
    print("no")
