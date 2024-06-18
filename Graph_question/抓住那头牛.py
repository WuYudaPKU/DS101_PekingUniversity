import heapq
N,K=map(int,input().split())
visited=[0 for _ in range(100001)]
methods=[(0,N)]
while True:
    method=heapq.heappop(methods)
    t,x=method

    if x==K:
        print(t)
        exit()

    visited[x]=t

    if x+1<=100000:
        if not visited[x+1]:heapq.heappush(methods,(t+1,x+1))
    if x-1>=0:
        if not visited[x-1]:heapq.heappush(methods,(t+1,x-1))
    if x*2<=100000:
        if not visited[x*2]:heapq.heappush(methods,(t+1,x*2))