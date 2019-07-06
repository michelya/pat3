times = int(input())
inData = input().split(' ')
count=0
sum=0
for  i in inData:
    try:
        if -1000.0<=float(i)<=1000.0:
            pass
        else:
            print('ERROR: {} is not a legal number',i)
    except expression as identifier:
       print('ERROR: {} is not a legal number',i)
   