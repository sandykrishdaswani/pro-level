or,kr=map(int,input().split())

pr=list(map(int,input().split()))

vr=list(map(int,input().split()))

tr=[]

cr=0

for i in range(or):

    xr=vr[i]/pr[i]

    t.append(xr)

while kr>=0 and len(tr)>0:

    mindex=tr.index(max(tr))

    if kr>=p[mindex]:

        cr=cr+vr[mindex]

        kr=kr-pr[mindex]

    pr.pop(mindex)

    vr.pop(mindex)

    tr.pop(mindex)

print(cr)
