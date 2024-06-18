class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def getGrades(self):
        return len(self.connectedTo)

    def is_connected_to(self,other):
        return other in self.connectedTo

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex

    def addEdge(self,v1,v2,weight=0):
        if v1 not in self.vertList:
            nv=self.addVertex(v1)
        if v2 not in self.vertList:
            nv=self.addVertex(v2)
        self.vertList[v1].addNeighbor(self.vertList[v2],weight)
        self.vertList[v2].addNeighbor(self.vertList[v1],weight)

G=Graph()
n,m=map(int,input().split())
for i in range(n):
    G.addVertex(i)
for _ in range(m):
    v1,v2=map(int,input().split())
    G.addEdge(v1,v2)

matrix_1=[[0 for _ in range(n)] for _ in range(n)]
matrix_2=[[0 for _ in range(n)] for _ in range(n)]
matrix_3=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix_1[i][i]=G.vertList[i].getGrades()

for i in range(n):
    for j in range(n):
        if G.vertList[i].is_connected_to(G.vertList[j]):
            matrix_2[i][j]=1
for i in range(n):
    for j in range(n):
        matrix_3[i][j]=matrix_1[i][j]-matrix_2[i][j]

for row in matrix_3:
    print(*row)