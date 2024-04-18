n,Price=map(int,input().split())
price_value=[tuple(map(int,input().split())) for _ in range(n)]
# 鉴于第i行值依赖且仅依赖于第i-1行值，所以可以遍历i次，
# 滚动地更新数组的值，通过时间上的覆盖取代了空间上的
# 记录，从而减少空间开销。
def KnapSack(price_value:list,n:int,Price:int):
    dp=[0 for _ in range(Price)]
    for i in range(n):
        price,value=price_value[i]
        for j in range(Price-1,price-1,-1):
            dp[j]=max(dp[j],dp[j-price]+value)
    return dp[-1]

print(KnapSack(price_value,n,Price))