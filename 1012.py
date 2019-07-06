nums = input().split()  
lens=int(nums[0])
nums=list(map(int,nums[1:])) 
outnums = [0, 0, 0, 0, 0]
count2 = 0
count4 = 0
for idx in range(lens):
    if nums[idx] % 5 == 0:
        outnums[0] += nums[idx] if nums[idx] % 2 == 0 else 0
    elif nums[idx] % 5 == 1:
        outnums[1] += (-1)**count2 * nums[idx]
        count2 += 1
    elif nums[idx] % 5 == 2:
        outnums[2] += 1
    elif nums[idx] % 5 == 3:
        outnums[3] += nums[idx]
        count4 += 1
    elif nums[idx] % 5 == 4:
        outnums[4] = nums[idx] if outnums[4] < nums[idx] else outnums[4]
outStr=''
for idx, outnum in enumerate(outnums):
    if idx!=1 and outnum==0:
        outStr+=' N'
        continue
    if idx==1 and count2 ==0: 
        outStr+=' N'
        continue
    if idx == 3:
        outStr+=' '+str(round((outnum / count4),1))
    else:
        outStr+=' '+str(outnum )
print(outStr.strip())