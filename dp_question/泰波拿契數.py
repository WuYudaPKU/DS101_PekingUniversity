from functools import lru_cache
@lru_cache(maxsize=None)
def T(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    return T(n-3)+T(n-2)+T(n-1)

print(T(int(input())))