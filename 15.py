sandy=input()
krish=map(int,input().split())
sea=[]
for i in krish:
    got=bin(i)
    sea.append(got)
fake=sorted(sea)
fake.reverse()
for j in fake:
    print(int(j,2))
