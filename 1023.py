numList=list(map(int,input().split()))
outstr=''
min=10
for idx,val in enumerate(numList):
    if val>0 and min>idx and idx!=0:
        min=idx
        break;
outstr+=str(min)       
for idx,val in enumerate(numList):
    if idx==min:
        outstr+=str(idx)*(val-1)
    else:
        outstr+=str(idx)*val
print(outstr)
    