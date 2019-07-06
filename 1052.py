import re
shou=[]
yan=[]
kou=[]
for i in range(3):
    instr=input()
    instr=instr.replace('[',' ')
    instr=instr.replace(']',' ')
    if i==0:
        shou=instr.strip().split()
    if i==1:
        yan=instr.strip().split()
    if i==2:
        kou=instr.strip().split()
times=int(input())
for i in range(times):
    inList=list(map(int,input()))
    for i in inList:
        if i>10:
            print('Are you kidding me? @\/@')
print(shou[inList[0]]+yan[[inList[1]]]+kou[[inList[2]]]+yan[[inList[3]]]+shou[[inList[1]]])
      