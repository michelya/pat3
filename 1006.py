num = input()
bai = int(num[-3:-2]) if len(num) == 3 else 0
shi = int(num[-2:-1]) if len(num) >= 2 else 0
ge = int(num[-1:])
print('B' * bai + 'S' * shi + "".join(str(i) for i in range(1, ge + 1)), end='')
