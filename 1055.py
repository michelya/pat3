from functools import cmp_to_key

def custom_sorted(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

print(sorted([2,3,1,5,4],key=cmp_to_key(custom_sorted)))
