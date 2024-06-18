import heapq,copy
class Vertex:
    def __init__(self,id):
        self.id=id
        self.neighbors={}
        self.previous=None
        self.color='white'

    def __lt__(self, other):
        return self.id<other.id

class Path:
    def __init__(self,weight,passer:list):
        self.weight=weight
        self.passer=passer
    def __lt__(self, other):
        return self.weight<other.weight

class Graph:
    def __init__(self):
        self.vertices={}
        self.num_vertices=0

    def add_vertex(self,id):
        self.vertices[id]=Vertex(id)
        self.num_vertices+=1

    def add_edge(self,v1:Vertex,v2:Vertex,weight:int):
        if v1.id not in self.vertices:
            self.vertices[v1.id]=v1
        if v2.id not in self.vertices:
            self.vertices[v2.id]=v2
        v1.neighbors[v2]=weight
        v2.neighbors[v1]=weight
        self.num_vertices+=1

def BFS(f:Vertex,t:Vertex):
    global graph
    q=[]
    init_path=Path(0,[f])
    heapq.heappush(q,init_path)
    while q:
        cur_path=heapq.heappop(q)
        cur_weight=cur_path.weight
        if cur_path.passer[-1]==t:return cur_path.passer
        cur_vert=cur_path.passer[-1]
        cur_vert.color='grey'
        for next_vert in cur_vert.neighbors:
            if next_vert.color=='white':
                new_path=Path(cur_weight,copy.deepcopy(cur_path.passer)+[next_vert])
                heapq.heappush(q,new_path)
        cur_vert.color='black'

graph=Graph()

P=int(input())
places=[input() for _ in range(P)]

Q=int(input())
for _ in range(Q):
    a,b,weight=map(str,input().split())
    if a in graph.vertices:v1=graph.vertices[a]
    else:v1=Vertex(a)
    if b in graph.vertices:v2=graph.vertices[b]
    else:v2=Vertex(b)
    graph.add_edge(v1,v2,int(weight))

R=int(input())
for _ in range(R):
    f,t=map(str,input().split())
    tmp1,tmp2,tmp3,res=BFS(graph.vertices[f],graph.vertices[t]),[],[],[]
    for i in tmp1:
        tmp2.append(graph.vertices[i.id])
    for i in range(1,len(tmp2)):
        f,t=tmp2[i-1],tmp2[i]
        tmp3.append('('+str(f.neighbors[t])+')')
    for _ in range(len(tmp3)):
        res.append(tmp2[_].id)
        res.append(tmp3[_])
    res.append(tmp2[-1].id)
    print('->'.join(res))