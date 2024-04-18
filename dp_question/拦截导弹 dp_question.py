import heapq
from collections import deque
n,heights,dp=int(input()),deque(map(int,input().split())),[]

# dp中存 （i前子列的最大长度，该子列的最小值）
heapq.heappush(dp,(-1,heights[0]))
pre_max=heights[0]
heights.popleft()

while heights:
    current_height=heights.popleft()
    if current_height>pre_max:
        pre_max=current_height
        heapq.heappush(dp,(-1,pre_max))
        continue

    buffer=[]
    while dp:
        tmp=heapq.heappop(dp)
        max_l,min_height=tmp
        if current_height<=min_height:
            heapq.heappush(dp,tmp)
            heapq.heappush(dp, (max_l-1,current_height))
            break
        else:
            buffer.append(tmp)
            continue
    for i in buffer:
        heapq.heappush(dp,i)

res=heapq.heappop(dp)
print(-res[0])