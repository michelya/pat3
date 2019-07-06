inList = []
sList = []
intimes = int(input())
for i in range(intimes):
    inList.append(input().split(' '))
stimes = int(input())
sList=input().split(' ')
for i in sList:
    for inData in inList:
        if i== inData[1]:
            print(inData[0] + ' ' + inData[2] ,end='\n')
