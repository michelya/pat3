nums = list(map(int,input().split()))
if nums[1] == 0:
    print(0, 0)
else:
    for i in range(len(nums) // 2):
        a = nums[2 * i]
        b = nums[2 * i + 1]
        if i == 0 and b > 0:
            print(a * b, b - 1, end='')
        elif b > 0:
            print(' ' + str(a * b), b - 1, end='')

