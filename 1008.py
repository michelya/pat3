aryLens, mov = map(int, input().strip().split(' '))
ary = input().strip().split(' ')
for i in range(0, mov):
    tmp = ary[aryLens - 1]
    for j in range(0, aryLens - 1):
        ary[aryLens - j - 1] = ary[aryLens - j - 2]
    ary[0] = tmp
print(' '.join(map(str, ary)))