from collections import deque
d=[(1,0),(-1,0),(0,1),(0,-1)]
X,Y=map(int,input().split())
graph=['1'*(Y+1)]+['1'+input() for _ in range(X)]

def BFS(graph):
    global X,Y,d
    start,end,key=None,None,None
    for i in range(1,X+1):
        for j in range(1,Y+1):
            if graph[i][j]=='R':start=(i,j)
            if graph[i][j]=='C':end=(i,j)
            if graph[i][j]=='Y':key=(i,j)

    # dq中的元素为（place(tuple)，flag(bool)，path(str)）
    dq=deque()
    dq.append((start, False, "".join(str(i) for i in start)))
    visited=[[False for j in range(Y+1)] for i in range(X+1)]
    visited[start[0]][start[1]]=True

    while dq:
        place,avail,path=dq.popleft()
        x,y=place
        if (x,y)==end and avail:return path
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if nx<=0 or nx>X or ny<=0 or ny>Y:continue
            if graph[nx][ny]=='1': continue
            if (nx,ny)==key:avail=True
            if visited[nx][ny] and not avail:continue
            visited[nx][ny]=True
            dq.append(((nx,ny),avail,path+str(nx)+str(ny)))
    return

ans=BFS(graph)
for i in range(0,len(ans),2):
    tmp=ans[i:i+2]
    print(' '.join(tmp))