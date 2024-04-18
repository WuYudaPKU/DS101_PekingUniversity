# dp
"""待入序列为a1,a2,...
dp[i]表示a1第i个出栈时总的序列数。
a1是栈底元素，a1第i个出，意味着前i-1的元素已经出完，出法有dp[i-1]个
而剩下的元素有dp[n-i]种排法。
也就是说dp[i]=dp[i-1]+dp[n-i]

边界条件是dp[0]==1.
"""
from functools import lru_cache
@lru_cache(maxsize=None)
def StackOut(n):
    if n==0:
        return 1
    ans=0
    for i in range(1,n+1):
        ans+=StackOut(i-1)*StackOut(n-i)
    return ans

n=int(input())
print(StackOut(n))