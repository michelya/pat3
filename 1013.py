from math import sqrt

primeList = [2]
nums = list(map(int, input().split()))
count = 2
rowFlag=1
while(len(primeList)<=nums[1]):
    isPrime = True
    for j in primeList:
        if (j > sqrt(count)):
            break
        if count % j == 0:
            isPrime = False
            break
    if isPrime:
        primeList.append(count)
        if len(primeList)>nums[0]:
            if rowFlag%10==0:
                print(primeList[len(primeList)-1],end='\n')
            elif len(primeList)>nums[1]:
                print(primeList[len(primeList)-1],end='')
            else:
                print(primeList[len(primeList)-1],end=' ')
            rowFlag+=1
    count+=1
  
