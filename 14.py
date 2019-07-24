sandy,uma=map(int,input().split())
list1=list(map(int,input().split()))
sandy=[]
list1.insert(0,0)
for y in range(uma):
     vin=[]
     s=0
     bb,zz=map(int,input().split())
     for i in range(bb,zz+1):         
         s^=list1[i]     
     sandy.append(s)
for y in sandy:
     print(y)
