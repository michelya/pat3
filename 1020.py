kinds,req=list(map(int,input().split()))
storeList=list(map(float,input().split()))
priceList=list(map(float,input().split()))
rate = {i: priceList[i]/storeList[i] for i in range(kinds)} 
order = sorted(rate, key=lambda i:rate[i], reverse=True)
count=0
for i in order:
    if req>=storeList[i]:
         count+=priceList[i]
         req-=storeList[i]
    else:
       count+=req*rate[i]
       break
print('%.2f' % count)

