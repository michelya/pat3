from math import sqrt

num = int(input())
pnum = 0
prime = 3
primeList = [2,3]
if num > 4:   
 for i in range(5, num + 1):
    isPrime = True
    for j in primeList:
        if (j > sqrt(i)):
            break
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        if (i - prime == 2):
            pnum += 1
        prime = i
        primeList.append(i)
print(pnum)