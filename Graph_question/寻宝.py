from collections import deque
m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(m)]
def BFS(graph):
    d=[(-1,0),(0,-1),(0,1),(1,0)]
    dq=deque()
    dq.append((0,0,0))
    while dq:
        x,y,cost=dq.popleft()
        if graph[x][y]==1:return cost
        graph[x][y]=2
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if nx<0 or nx>=m or ny<0 or ny>=n or graph[nx][ny]==2:
                continue
            dq.append((nx,ny,cost+1))
    return 'NO'
print(BFS(graph))