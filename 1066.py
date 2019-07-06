inNums = list(map(int, input().split()))
c = str(inNums[4]).zfill(3)  
for i in range(inNums[0]):
    inputNums=input().split()
    outStr=''
    for j in range(inNums[1]):
        rowNum=int(inputNums[j])
        if inNums[2] <= rowNum <= inNums[3]:
            outStr+=' '+c
        else:
            outStr+=' '+str(rowNum).zfill(3)
    
    print(outStr.lstrip())