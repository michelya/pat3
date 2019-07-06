inputStr = input().rstrip().split(" ")
length = len(inputStr)
while length > 0:
    if length != 1:
        print(inputStr[length - 1], end=' ')
    else:
        print(inputStr[length - 1], end='')
    length = length - 1
