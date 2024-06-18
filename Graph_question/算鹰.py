visited=[[False for _ in range(10)] for _ in range(10)]
board=[list(input()) for _ in range(10)]
# 这里dfs函数的功能是探出所有连通区域，并打上标记
steps=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y):
    visited[x][y]=True
    for dx,dy in steps:
        nx,ny=x+dx,y+dy
        if 0<=nx<10 and 0<=ny<10 and not visited[nx][ny] and board[nx][ny]=='.':
            dfs(nx,ny)
cnt=0
for x in range(10):
    for y in range(10):
        if board[x][y]=='-':
            visited[x][y]=True
for x in range(10):
    for y in range(10):
        if board[x][y]=='.' and not visited[x][y]:
            cnt+=1
            dfs(x,y)
print(cnt)
