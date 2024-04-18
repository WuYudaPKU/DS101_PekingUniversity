from functools import lru_cache
@lru_cache(maxsize=None)
def draw_CantorSet(n):
    if n==1:
        return '*-*'
    last=draw_CantorSet(n-1)
    return last+'-'*3**(n-1)+last

print(draw_CantorSet(int(input())))