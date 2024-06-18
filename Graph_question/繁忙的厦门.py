# kruskal
class DisjointSet:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1


def kruskal(graph,n):
    # 图形如：graph[1]={2:5,3:1,...}
    cnt,ans,djs,edges=0,0,DisjointSet(len(graph)),[]
    visited=set()
    for v1 in graph:
        for v2 in graph[v1]:
            weight=graph[v1][v2]
            if not ((v1,v2) in visited or (v2,v1) in visited):
                edges.append((weight,v1,v2))
                visited.add((v1,v2))
    edges.sort(key=lambda x:x[0])

    for i in edges:
        weight,u,v=i
        if djs.find(u)!=djs.find(v):
            djs.union(u,v)
            cnt+=1
            ans=max(ans,weight)

    return cnt,ans

n,m=map(int,input().split())
graph={i:{} for i in range(n+1)}
for _ in range(m):
    u,v,c=map(int,input().split())
    graph[u][v]=graph[v][u]=c
cnt,ans=kruskal(graph,n)
print(cnt,ans)