import sys,heapq
class Vertex:
    def __init__(self,id):
        self.id=id
        self.connectedTo={}
        self.distance=sys.maxsize
        self.pre=None

    def __str__(self):
        return '*'+self.id

    def add_neighbor(self,nbr,weight):
        self.connectedTo[nbr]=weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __lt__(self, other):
        return self.distance<other.distance

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

    def __str__(self):
        return " ".join(map(str,self.vertList.values()))

    def addVertex(self,key):
        if key in self.vertList:return

        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        self.numVertices+=1
        return newVertex

    def getVertex(self,key):
        return self.vertList[key]

    def addEdge(self,f:str,t:str,weight):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].add_neighbor(self.vertList[t],weight)
        self.vertList[t].add_neighbor(self.vertList[f],weight)

def prim(start:Vertex):
    pq,visited=[],set()
    start.distance=0
    heapq.heappush(pq,(0,start))
    while pq:
        curDist,curVert=heapq.heappop(pq)
        if curVert in visited:
            continue
        visited.add(curVert)
        for nextVert in curVert.getConnections():
            weight=curVert.getWeight(nextVert)
            if nextVert not in visited and weight<nextVert.distance:
                nextVert.distance=weight
                nextVert.pre=curVert
                heapq.heappush(pq,(weight,nextVert))
    return start

def Tree_summing(graph:Graph):
    res=0
    for vert in graph.vertList.values():
        if vert.pre:res += vert.connectedTo[vert.pre]
    return res

n=int(input())
graph=Graph()
for i in range(n-1):
    raw=list(input().split())
    curVert=raw[0]
    graph.addVertex(curVert)
    data=raw[2:]
    for j in range(len(data)//2):
        new_VertKey=data[2*j]
        new_VertWeight=int(data[2*j+1])
        graph.addEdge(curVert,new_VertKey,new_VertWeight)

start=None
for i in graph.vertList.values():
    start=i
    break
prim(start)
print(Tree_summing(graph))