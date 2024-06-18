from collections import deque
for _ in range(T:=int(input())):
    N,M=map(int,input().split())
    # 邻接表，入度
    graph={i:[] for i in range(1,N+1)}
    in_degree=[0 for i in range(N+1)]
    # from,to
    for i in range(M):
        f,t=map(int,input().split())
        graph[f].append(t)
        in_degree[t]+=1

    q,cnt=deque(),0
    for i in range(1,N+1):
        if in_degree[i]==0:
            q.append(i)
    while q:
        cur=q.popleft()
        cnt+=1
        for vert in graph[cur]:
            in_degree[vert]-=1
            if in_degree[vert]==0:
                q.append(vert)

    print('No' if cnt==N else "Yes")