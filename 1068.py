import numpy as np
count=0 
outStr=''
point=''
locations=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
inputNums=[]
countNums=[]
def isColor(i,j,nums):
    isColor=True
    for  location in locations:
        x=i+location[0]
        y=j+location[1]
        if x>=0 and x<inNums[1] and y>=0 and y<inNums[0]\
            and nums-inputNums[x][y]<=inNums[2] \
            and nums - inputNums[x][y] >= 0 - inNums[2]:
            isColor=False
    return isColor

inNums = list(map(int, input().split()))   
for row in range(inNums[1]):
    inputNums.append([int(j) for j in input().split()])
    countNums.extend(inputNums[row])
for row in range(inNums[1]):
    for col in range(inNums[0]):
        if countNums.count(inputNums[row][col])==1 and  isColor(row,col,inputNums[row][col]):
            outStr+='('+str(col+1)+', '+str(row+1)+'): '+str(inputNums[row][col])
            count+=1
if count==0:
    print('Not Exist')
if count>1:    
    print('Not Unique')
if count==1:    
    print(outStr)