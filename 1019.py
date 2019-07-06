n=input()
n=n.zfill(4)
if n[0] == n[1] == n[2] == n[3]:
    print('{0} - {0} = 0000'.format(n))
else:
    while 1:
        tmpList=list(n)
        tmpList.sort(reverse=True)
        n1Str=''.join(tmpList)
        tmpList.sort(reverse=False)
        n2Str=''.join(tmpList)
        n1=int(n1Str)
        n2=int(n2Str)
        n=str(n1-n2).zfill(4)
        print( n1Str,'-',n2Str,'=',n,end='\n')
        if n == '6174':
            break