num=input()
for i in range(10):
    times=num.count(str(i))
    if times>0:
        print(str(i)+':'+str(times),end='\n')