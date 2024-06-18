class Vertex:
    def __init__(self,key,weight):
        self.id=key
        self.weight=weight
        self.connectedTo={}
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0
    def addVertex(self,key,weight):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key,weight)
        self.vertList[key]=newVertex
    def addEdge(self,v1,v2,weight=0):
        self.vertList[v1].addNeighbor(self.vertList[v2],weight)
        self.vertList[v2].addNeighbor(self.vertList[v1],weight)


def dfs(vert_id,visited):
    vert=G.vertList[vert_id]
    if visited[vert.id]:return 0
    weight,visited[vert.id]=vert.weight,True
    if not vert.connectedTo:
        return weight

    for son_vert in vert.connectedTo:
        son_id=son_vert.id
        weight+=dfs(son_id,visited)
    return weight

def MaxAdjWeights(graph):
    weights,visited = [],[False for _ in range(n)]
    for vert_id in graph.vertList:
        if not visited[vert_id]:
            weights.append(dfs(vert_id,visited))
    return max(weights)

G=Graph()
n,m=map(int,input().split())
vert_weight=list(map(int,input().split()))

for id,weight in enumerate(vert_weight):
    G.addVertex(id,weight)

for _ in range(m):
    v1,v2=map(int,input().split())
    G.addEdge(v1,v2)

print(MaxAdjWeights(G))