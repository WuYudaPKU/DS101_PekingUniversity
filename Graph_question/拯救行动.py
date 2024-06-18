from heapq import heappush, heappop
move=[(0,1),(1,0),(0,-1),(-1,0)]
def GuardPrincess(graph,N,M):
    # graph为矩阵形式,N行M列。
    global move
    pq,knight,princess=[],None,None
    for i in range(N):
        for j in range(M):
            if graph[i][j]=='r':
                knight=(i,j)
            if graph[i][j]=='a':
                princess=(i,j)

    heappush(pq,(0,knight[0],knight[1]))
    while pq:
        curtime,x,y=heappop(pq)
        if (x,y)==princess:
            return curtime

        for dx,dy in move:
            nx,ny=x+dx,y+dy
            if nx<0 or nx>=N or ny<0 or ny>=M:continue
            if graph[nx][ny]=='#':continue
            ntime=curtime+1
            if graph[nx][ny]=='x':ntime+=1
            heappush(pq,(ntime,nx,ny))
            graph[nx][ny]='#'
    return 'Impossible'

for _ in range(int(input())):
    N,M=map(int,input().split())
    graph=[list(input()) for _ in range(N)]
    print(GuardPrincess(graph,N,M))