datas = input().split(' ')
for i in range(round(int(datas[0]) / 2+0.4)):
    if i==0 or i==round(int(datas[0]) / 2+0.4)-1:
        print(datas[1] * int(datas[0]), end='\n')
    else:
        print(datas[1] + ' ' * (int(datas[0])-2) + datas[1], end='\n')
