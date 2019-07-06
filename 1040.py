inStr = input()
std = 'PAT'
count = 0
for idx,val in enumerate(inStr):
    if val != 'P':
        continue
    else:
        tmp = val
        for j in inStr[idx + 1:]:
            if std.startswith(tmp+j):
                tmp += j
            if tmp == std:
                count += 1
print(count % 1000000007)
