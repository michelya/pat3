times = int(input())
jia = [0, 0, 0, 0, 0, 0]
yi = [0, 0, 0, 0, 0, 0]
t = ['B', 'C', 'J']


def judge(lst, jia, yi):
    jwin = ['BC', 'CJ', 'JB']
    ywin = ['CB', 'JC', 'BJ']
    if lst[0] == lst[1]:
        jia[1] += 1
        yi[1] += 1
        return 0
    try:
        idx = jwin.index(''.join(lst))
    except ValueError:
        idx = -1
    try:
        idx1 = ywin.index(''.join(lst))
    except ValueError:
        idx1 = -1   
    if idx != -1:
        jia[0] += 1
        yi[2] += 1
        jia[3 + idx] += 1
    if idx1 != -1:
        jia[2] += 1
        yi[0] += 1
        yi[3 + idx1] += 1

for i in range(times):
    lst = [i for i in input().split()]
    judge(lst, jia, yi)
print(jia[0], jia[1], jia[2], end='\n')
print(yi[0], yi[1], yi[2], end='\n')
print(t[jia[3:].index(max(jia[3:]))], t[yi[3:].index(max(yi[3:]))])
