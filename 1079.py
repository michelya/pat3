N = input()
count = 0
while 1:
    if N == N[::-1]:
        print(N, 'is a palindromic number.')
        break
    elif count >= 10:
        print('Not found in 10 iterations.')
        break
    else:
        print(N, '+', N[::-1], '=', str(int(N) + int(N[::-1])), end='\n')
        N = str(int(N) + int(N[::-1]))
        count+=1
