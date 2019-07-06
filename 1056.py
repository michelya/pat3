strs = input().split(' ')
nums = set()
for i in range(1,len(strs)):
    for j in range(1,len(strs)):
        if i == j:
            continue
        nums.add(int(strs[i] + strs[j]))
print(sum(nums))