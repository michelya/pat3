intimes = int(input())
inDatas =[]
jia=0
yi=0
for i in range(intimes):
    inDatas.append(list(map(int,input().split(' '))))
for inData in inDatas:
    sumNum=inData[0]+inData[2]
    if inData[1]==sumNum and inData[3]==sumNum:
        continue    
    if inData[1]==sumNum:
        yi+=1
    if inData[3]==sumNum:
        jia+=1
print(str(jia)+' '+str(yi))