list = []
for i in range(4):
    list.append(input())
weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
outputStr = ''
pairs = 0
for idx, k in enumerate(list[0]):
    if ord('A') <= ord(k) <= ord(
            'G') and list[0][idx:idx + 1] == list[1][idx:idx +
                                                     1] and pairs == 0:
        outputStr += weeks[ord(k) - ord('A')] + ' '
        pairs += 1
        continue
    if (ord('0')<=ord(k)<=ord('9') or ord('A')<=ord(k)<=ord('N')) \
        and list[0][idx:idx+1] == list[1][idx:idx+1] and pairs>0:
        if ord('A')<=ord(k)<=ord('N'):
            outputStr += str(10 + ord(k) - ord('A')) + ':'
        else:
            outputStr += str(ord(k) - ord('0') + 1).zfill(2) + ':'
        break
for idx, k in enumerate(list[2]):
    if ord('a') <= ord(k) <= ord('z') or ord('A') <= ord(k) <= ord('Z'):
        if list[2][idx:idx + 1] == list[3][idx:idx + 1]:
            outputStr += str(idx).zfill(2)
            break
print(outputStr)
