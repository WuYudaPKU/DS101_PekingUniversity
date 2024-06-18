from heapq import heappop, heappush
n,m=map(int,input().split())
graph={i:{} for i in range(n+1)}
distance=[float('inf') for _ in range(n+1)]
visited=[False for i in range(n+1)]

for _ in range(m):
    u,v,c=map(int,input().split())
    graph[u][v]=graph[v][u]=c

ans,cnt,pq,distance[1]=0,0,[(0,0,1)],0
while pq:
    # 三元组：(当前节点与起点距离，当前节点与上一个节点连线权值，当前节点)。
    d,cur,vert=heappop(pq)
    if not visited[vert]:
        visited[vert]=True
        ans=max(ans,cur)
        cnt+=1
        # next vert
        for nv in graph[vert]:
            if not visited[nv]:
                distance[nv]=min(distance[nv],distance[vert]+graph[vert][nv])
                heappush(pq,(distance[nv],graph[vert][nv],nv))
# 起点多记了一次，减去。
print(cnt-1,ans)