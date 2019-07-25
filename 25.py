def LIS(arr,size):
    krish=[]
    count=1
    for i in range(0,size-1):
        if arr[i]<arr[i+1]:
            count+=1
        else:
            krish.append(count)
            count=1
    krish.append(count)
    print(max(krish))
size=int(input())
arr=list(map(int,input().split()))
LIS(arr,size)
