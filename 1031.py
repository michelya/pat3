import re
global intab
intab = list("0 1 2 3 4 5 6 7 8 9 10".split(' '))
global outtab
outtab = list("1 0 X 9 8 7 6 5 4 3 2".split(' '))
global quan
quan = list(map(int, '7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2'.split(',')))


def vaildIdcard(idcard):
    global intab
    global outtab
    global quan
    retFlag = True
    if not idcard[:17].isdigit():
        retFlag = False
        return retFlag
    sumNub = 0
    for idx, i in enumerate(idcard[:17]):
        sumNub += int(i) * quan[idx]
    modNum = sumNub % 11
    mapModNum = outtab[intab.index(str(modNum))]
    if mapModNum != idcard[-1]:
        retFlag = False
    return retFlag


times = input()
count = 0
for i in range(int(times)):
    idcard = input()
    if not vaildIdcard(idcard):
        print(idcard, end='\n')
        count += 1
if (count == 0):
    print('All passed')
