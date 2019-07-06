A,B,D=map(int,input().split())
count=A+B
outstr=''
while 1:
  if count//D==0:
    outstr+=str(count)
    break  
  yu=count%D  
  count=count//D
  outstr+=str(yu)
print(outstr[::-1])
