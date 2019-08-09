sandy=int(input())
isi=0
xsy=0
bs=[]
while isi<90 and isi<sandy:

  ss=0

  for j in str(sandy-isi):

    ss+=int(j)

  if ss+(sandy-isi)==sandy:

    xsy+=1

    bs.append(sandy-isi)

  isi+=1

print(xsy)

for isi in bs:

  print(isi)
