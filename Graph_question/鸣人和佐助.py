import heapq
M,N,T=map(int,input().split())
graph=[list(input()) for _ in range(M)]
visited=[[-1 for _ in range(N)] for _ in range(M)]
start,end=None,None
for i in range(M):
    for j in range(N):
        if graph[i][j]=='@':
            start=(i,j)
        if graph[i][j]=='+':
            end=(i,j)

def BFS(start,end,tools):
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    x,y=start
    visited[x][y],pq,steps=tools,[],0
    heapq.heappush(pq,(steps,x,y))
    while pq:
        tmp_step,x,y=heapq.heappop(pq)
        if (x,y)==end:
            return steps
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            # 不越界
            if (0<=nx<M and 0<=ny<N):
                # 若为'*'
                if graph[nx][ny]=='*' and visited[x][y]>visited[nx][ny]:
                    visited[nx][ny]=visited[x][y]
                    heapq.heappush(pq,(tmp_step+1,nx,ny))
                # 若为'#'
                elif graph[nx][ny]=='#' and visited[x][y]-1>visited[nx][ny]:
                    visited[nx][ny]=visited[x][y]-1
                    heapq.heappush(pq,(tmp_step+1,nx,ny))
                elif graph[nx][ny]=='+':return tmp_step+1
    return -1

print(BFS(start,end,T))