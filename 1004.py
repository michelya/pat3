times = int(input())
inputAry = []
for i in range(0, times):
    inputAry.append(input().split(' '))
maxIdx = 0
minIdx = 0
for i in range(0, len(inputAry) - 1):
    if int(inputAry[maxIdx][2]) < int(inputAry[i][2]):
        maxIdx = i
    if int(inputAry[minIdx][2]) > int(inputAry[i][2]):
        minIdx = i
print(inputAry[maxIdx][0] + ' ' + inputAry[maxIdx][1], end='\n')
print(inputAry[minIdx][0] + ' ' + inputAry[minIdx][1], end='\n')
