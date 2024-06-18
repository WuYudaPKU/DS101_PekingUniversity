from heapq import heappop, heappush
while True:
    try:N=int(input())
    except EOFError:break
    distance=[[int(i) for i in input().split()] for _ in range(N)]
    cost=[float('inf')]*N
    q,solved=[(0,0)],[False]*N
    ans,cost[0]=0,0

    while q:
        c,a=heappop(q)
        if not solved[a]:
            ans+=c
            solved[a]=True
            for i in range(N):
                if not solved[i]:
                    cost[i]=min(cost[i],distance[a][i])
                    heappush(q,(cost[i],i))
    print(ans)