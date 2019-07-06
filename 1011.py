times = int(input())
groups = []
for i in range(times):
    groups.append(list(map(int, input().strip().split())))
count = 1
for  nums in groups:
    if nums[0] + nums[1] > nums[2]:
        print('Case #' + str(count) + ': true',end='\n')
    else:
        print('Case #' + str(count) + ': false',end='\n')
    count += 1
