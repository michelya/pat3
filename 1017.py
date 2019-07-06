a, b = map(int, input().split())
q = a // b
r = a % b
if (b * q + r == a):
    print(q, r)
