N, F = input().split()
N = int(N)
i = 1
count = 0
while 1:
    if (count+ i*2+1)*2+1<=N:
       count += i * 2 + 1
       i+=1
    else:
       break;
      
remain = N - (count*2+1) if i>1  else N
firstRow= (i-1)*2+1
if firstRow>=3:
   space = 0
   for j in range(firstRow, 0, -2):
      print(' ' * space + F * j, end='\n')
      space += 1
   space -= 1
   for k in range(3, firstRow+1, 2):    
      space -= 1
      print(' ' * space + F * k, end='\n')
print(remain)
