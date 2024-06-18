import sys
sys.setrecursionlimit(1000000)
def dfs(graph,start:tuple):
    # 负责把所有遍历到的W打成visited
    global visited,steps,steps,N,M
    x,y=start
    if x<0 or x>=N or y<0 or y>=M or visited[x][y] or graph[x][y]=='.':
        return False
    else:
        visited[x][y]=True
        for step in steps:
            dx,dy=step
            nx,ny=x+dx,y+dy
            dfs(graph,(nx,ny))
    return True

N,M=map(int,input().split())
graph=[input() for _ in range(N)]
visited=[[False for i in range(M)] for _ in range(N)]
steps=[(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]

cnt=0
for i in range(N):
    for j in range(M):
        if dfs(graph,(i,j)):
            cnt+=1
print(cnt)