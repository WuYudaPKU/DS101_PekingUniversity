from collections import deque
class Vertex:
    def __init__(self,id):
        self.id=id
        self.neighbors={}
        # 当找到路径后，通过Previous用于显式地把路径体现出来
        self.previous=None
        self.color='white'
    def __str__(self):
        return '*'+self.id
class Graph:
    def __init__(self):
        self.vertices={}
        self.num_vertices=0

    def add_vertex(self,id):
        self.vertices[id]=Vertex(id)
        self.num_vertices+=1

    def add_edge(self,v1_id,v2_id):
        # v1_start,v2_end
        if v1_id not in self.vertices:
            self.vertices[v1_id]=Vertex(v1_id)
        if v2_id not in self.vertices:
            self.vertices[v2_id]=Vertex(v2_id)
        v1,v2=self.vertices[v1_id],self.vertices[v2_id]
        v1.neighbors[v2_id]=v2
        self.num_vertices+=1

n,graph,buckets=int(input()),Graph(),{}
words=[input() for _ in range(n)]
for word in words:
    for bit in range(1,len(word)+1):
        tag=word[:bit-1]+'_'+word[bit:]
        bucket=buckets.setdefault(tag,set())
        bucket.add(word)
# for i,j in buckets.items():
#     print(i,j)
for bucket in buckets.values():
    for i in bucket:
        tmp=bucket-{i}
        for j in tmp:
            graph.add_edge(i,j)


start,goal=map(str,input().split())
# BFS,这里不用函数实现
q=deque()
q.append(graph.vertices[start])
current=graph.vertices[start]
# 注：标黑色用于把回头路堵死；标灰色用于把更长的可行路径堵死。
# 由于更长的可行路径被堵死且最短路径唯一，所以每个点的前驱若有有则仅有一个。
while q and current.id!=goal:
    current=q.popleft()
    for vert in current.neighbors.values():
        if vert.color=='white':
            vert.color='grey'
            vert.previous=current
            q.append(vert)
    current.color='black'

def traverse(start:Vertex):
    output=[start.id]
    current=start
    while current.previous:
        output.append(current.previous.id)
        current=current.previous
    return " ".join(output[::-1])

if current.id==goal:print(traverse(graph.vertices[goal]))
else:print("NO")