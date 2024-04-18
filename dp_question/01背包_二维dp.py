from functools import lru_cache
n,Price=map(int,input().split())
price_value=[(0,0)]
for _ in range(n):
    price_value.append(tuple(map(int,input().split())))
price_value.sort(key=lambda x:x[0])

@lru_cache(maxsize=None)
def backpack(i,j):
    if i==0 or j==0:return 0

    if price_value[j][0]<=i:
        return max(backpack(i,j-1),
                   backpack(i-price_value[j][0],j-1)+price_value[j][1])
    else:return backpack(i,j-1)

print(backpack(Price,n))