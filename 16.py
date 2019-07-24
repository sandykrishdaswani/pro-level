sandy1=int(input())
cat=list(map(int,input().split()))
y=[1]*sandy1
for i in range(sandy1):
    if i==0:
        if cat[i]>cat[i+1]:
            y[i]=y[i]+y[i+1]
    elif i>0:
        if cat[i]>c[i-1]:
            y[i]=y[i]+y[i-1]
print(sum(y))
