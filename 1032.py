N=int(input())
lst=[]
for i in range(N):
    lst.append(list(map(int,input().split())))
k={}
max=0
for l in lst:
   if l[0] in k.keys():
       k[l[0]]+=l[1]
   else:
       k[l[0]]=l[1]
k=sorted(k.items(), key=lambda d: d[1],reverse=True)
print(k[0][0],k[0][1])