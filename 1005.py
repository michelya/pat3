inputNumber = int(input())
nums = list(map(int, input().split(' ')))
nums1 = nums[:]
for inputNumber in nums1:
    while inputNumber != 1:
        if inputNumber % 2 == 0:
            inputNumber = inputNumber / 2
            if inputNumber in nums:
                nums.remove(inputNumber)
        else:
            inputNumber = (inputNumber * 3 + 1) / 2
            if inputNumber in nums:
                nums.remove(inputNumber)
nums.sort(reverse=True)
print(" ".join(str(i) for i in nums))
