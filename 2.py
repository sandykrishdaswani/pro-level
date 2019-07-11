sandy1,sandy2=input().strip().split(" ")
sandy2=int(sandy2)
j=0;
while j<len(sandy1)-1 and sandy2:
    if(sandy1[j]>sandy1[j+1]):
        sandy2-=1
        sandy1=sandy1[:j]+sandy1[j+1:]
        if(j!=0):
            j-=1
    else:
        j+=1
sandy=sandy1[:len(sandy1)-sandy2]
print(sandy)
