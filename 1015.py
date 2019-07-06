from functools import cmp_to_key

N, L, H = map(int, input().split())
scoreList = []


def cmpCai(x, y):
    if (x[1] + x[2]) > (y[1] + y[2]):
        return 1
    elif (x[1] + x[2]) < (y[1] + y[2]):
        return -1
    elif (x[1] + x[2]) == (y[1] + y[2]):
        if x[1] > y[1]:
            return 1
        elif x[1] < y[1]:
            return -1
        elif x[1] == y[1]:
            if x[0] > y[0]:
                return -1
            elif x[0] < y[0]:
                return 1
            else:
                return 0


for i in range(N):
    scoreList.append(list(map(int, input().split())))
decai = sorted(list(filter(lambda x: x[1] >= H and x[2] >= H, scoreList)),
               key=cmp_to_key(cmpCai),
               reverse=True)
dedacai = sorted(list(filter(lambda x: x[1] >= H and L<= x[2] < H, scoreList)),
                 key=cmp_to_key(cmpCai),
                 reverse=True)
decaijige = sorted(list(
    filter(lambda x: L<= x[1] < H and L<= x[2] < H and x[1]>x[2],
           scoreList)),
    key=cmp_to_key(cmpCai),
    reverse=True)
decaijige1 = sorted(list(
    filter(lambda x: L<= x[1] < H and L<= x[2]  and x[1]<=x[2],
           scoreList)),
    key=cmp_to_key(cmpCai),
    reverse=True)
decai.extend(dedacai)
decai.extend(decaijige)
decai.extend(decaijige1)
print(len(decai))
for score in decai:
    print(score[0], score[1], score[2], end='\n')
