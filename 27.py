o,kr=map(int,input().split())

pr=list(map(int,input().split()))

vr=list(map(int,input().split()))

tr=[]

cr=0

for i in range(o):

    xr=vr[i]/pr[i]

    tr.append(xr)

while kr>=0 and len(tr)>0:

    mindex=tr.index(max(tr))

    if kr>=pr[mindex]:

        cr=cr+vr[mindex]

        kr=kr-pr[mindex]

    pr.pop(mindex)

    vr.pop(mindex)

    tr.pop(mindex)

print(cr)
