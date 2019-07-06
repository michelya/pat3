inputNumber = input()
sumNum = 0
outPutStr = ''
upperNum = ['yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu', 'ling']
for num in inputNumber:
    sumNum += int(num)
for sumStr in str(sumNum):
    outPutStr += upperNum[int(sumStr) - 1] + ' '
print(outPutStr.rstrip())
