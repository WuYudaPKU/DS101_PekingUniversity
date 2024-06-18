from collections import defaultdict
from heapq import heappop, heappush

def Kahn(graph):
    q,ans,ind=[],[],defaultdict(int)
    for dic in graph.values():
        for vert in dic.keys():
            ind[vert]+=1
    for vert in graph.keys():
        if vert not in ind or ind[vert]==0:
            heappush(q,vert)
    while q:
        vertex=heappop(q)
        ans.append(vertex)
        for neighbor in graph[vertex]:
            ind[neighbor]-=1
            if ind[neighbor]==0:
                heappush(q,neighbor)
    return ans

n,m=map(int,input().split())
graph={i:{} for i in range(n)}
for _ in range(m):
    start,to=map(int,input().split())
    graph[start][to]=1

ans,cnt=Kahn(graph),0
for i in range(n):
    cur=ans[i]
    ne=len(graph[cur])
    cnt+=n-i-1-ne
print(cnt)