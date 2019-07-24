sandy,uma=map(int,input().split())
umasandy=list(map(int,input().split()))
l1=[]
for i in range(0,uma):
     a,b=map(int,input().split())
     l1.append([a,b])
for i in range(uma):
     lower=l1[i][0]
     upper=l1[i][1]
     x=sum(umasandy[lower-1:upper])
     print(x)
