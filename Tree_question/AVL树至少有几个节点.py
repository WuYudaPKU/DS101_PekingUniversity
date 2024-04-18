from functools import lru_cache
@lru_cache(maxsize=None)
def AVL(depth):
    if depth==1:return 1
    if depth==2:return 2
    return AVL(depth-1)+AVL(depth-2)+1
print(AVL(int(input())))