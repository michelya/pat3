t, n = input().split()
t = int(t)
n = int(n)
for i in range(n):
    lst = [int(j) for j in input().split()]
    if t < lst[2]:
        print('Not enough tokens.  Total = ' + str(t) + '.')
    else:
        if (lst[0] > lst[3] and lst[1] == 0) or (lst[0] < lst[3]
                                                 and lst[1] == 1):
            print('Win ' + str(lst[2]) + '!  Total = ' + str(t + lst[2]) + '.')
            t += lst[2]
        elif (lst[0] > lst[3] and lst[1] == 1) or (lst[0] < lst[3]
                                                   and lst[1] == 0):
            print('Lose ' + str(lst[2]) + '.  Total = ' +
                  str(t - int(lst[2])) + '.')
            t -= lst[2]
            if t <= 0:
                print('Game Over.')
                break
account, times = map(int, input().split())
for i in range(times):
    inList = [int(j) for j in input().split()]
    if inList[2] > account:
        print('Not enough tokens.  Total = ' + str(account) + '.')
    else:
        if (inList[3] > inList[0] and inList[1] == 1) or (inList[3] < inList[0]
                                                          and inList[1] == 0):
            account += inList[2]
            print('Win ' + str(inList[2]) + '!  Total = ' + str(account) + '.')
        elif (inList[3] > inList[0]
              and inList[1] == 0) or (inList[3] < inList[0]
                                      and inList[1] == 1):
            account -= inList[2]
            print('Lost ' + str(inList[2]) + '.  Total = ' + str(account) +
                  '.')
    if account <= 0:
        print('Game Over.')
        break
