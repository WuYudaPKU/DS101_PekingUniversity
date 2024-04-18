T,M=map(int,input().split())
raw=[]
dp=[[0 for _ in range(M+1)] for _ in range(T+1)]
for _ in range(M):
    raw.append(tuple(map(int,input().split())))
raw.sort(key=lambda x:x[0])
for i in range(1,T+1):
    for j in range(1,M+1):
        t,v=raw[j-1]
        if t>i:dp[i][j]=dp[i][j-1]
        else:dp[i][j]=max(dp[i][j-1],dp[i-t][j-1]+v)

print(dp[-1][-1])