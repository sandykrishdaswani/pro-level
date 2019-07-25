sandy,krish=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
san=0
total=krish
for i in arr:
    if total>=i:
        rem=int(total/i)
        san+=rem
        total=total - (i*rem)
    if total==0:
        break
if total==0:
    print(san)
else:
    print("it's not possible to sum up coins in such a way that they um upto",krish)
