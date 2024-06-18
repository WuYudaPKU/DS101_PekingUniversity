from heapq import heappush, heappop
from collections import defaultdict
import math
def dis(start,end):
    x1,y1=start
    x2,y2=end
    return round(math.sqrt((x2/1000-x1/1000)**2+(y2/1000-y1/1000)**2),5)
def walk(start,end):
    return dis(start,end)/10
def subway(start,end):
    return dis(start,end)/40
sx,sy,ex,ey=map(int,input().split())
# graph[(sx,sy)]==[]
graph=defaultdict(list)
graph[(sx,sy)],graph[(ex,ey)]=[],[]

while True:
    try:line=list(map(int,input().split()))
    except:break
    stations=[(line[i],line[i+1]) for i in range(0,len(line),2)]
    for i in range(len(stations)-1):
        s1,s2=stations[i],stations[i+1]
        if s1==(-1,-1) or s2==(-1,-1):continue
        graph[s1].append(s2)
        graph[s2].append(s1)

def dijkstra(graph,start,end):
    visited=set()
    pq=[(0,start[0],start[1])]
    while pq:
        time,x,y=heappop(pq)
        visited.add((x, y))
        if (x,y)==end:
            return time
        for nx,ny in graph:
            if (nx,ny) not in visited:
                walktime=walk((x,y),(nx,ny))
                subtime=subway((x,y),(nx,ny))
                if not graph[(x,y)]:
                    heappush(pq,(time+walktime,nx,ny))
                else:
                    heappush(pq,(time+min(walktime,subtime),nx,ny))

print('{:.0f}'.format(dijkstra(graph,(sx,sy),(ex,ey))*60))