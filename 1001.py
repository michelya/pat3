inputNumber = int(input())
step = 0
while inputNumber != 1:
    if inputNumber % 2 == 0:
        inputNumber = inputNumber / 2
    else:
        inputNumber = (inputNumber * 3 + 1) / 2
    step += 1
print(step)
