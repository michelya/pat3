nums = list(input().split(' '))
atimes=nums[0].count(nums[1])
btimes=nums[2].count(nums[3])
anum = int(nums[1] * atimes) if atimes>0 else 0  
bnum = int(nums[3] * btimes) if btimes>0 else 0  
print(anum + bnum)
