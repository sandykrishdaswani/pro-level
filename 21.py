import statistics as st
count1=int(input())
arr=list(map(int,input().split()))
hint=False
for i in range(1,count1):
    l1=arr[:i]
    l2=arr[i:]
    if st.mean(l1)==st.mean(l2):
        hint=True
if hint==True:
    print("yes")
else:
    print("no")
