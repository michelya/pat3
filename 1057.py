inStr=input().upper().strip()
count=0
for inChar in inStr:
    if inChar.isalpha():
        count+=ord(inChar)-ord('A')+1
if count==0:
     print('0 0')
else:
    outStr='{:b}'.format(count)
    print(outStr.count('0'),outStr.count('1'))