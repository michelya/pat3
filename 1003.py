import re

times = int(input())
inputAry = []
for i in range(0, times):
    inputAry.append(input())
for inputStr in inputAry:
    if re.match(r"A*PA*ATA*", inputStr):
        regroup = re.match(r"(A*)P(A*)AT(A*)", inputStr)
        groupA = regroup.group(1)
        groupB = regroup.group(2)
        groupC = regroup.group(3)
        if len(groupA) * (len(groupB)+1) == len(groupC):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
