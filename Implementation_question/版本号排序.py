import heapq
generations=[]
for _ in range(N:=int(input())):
    heapq.heappush(generations,tuple(map(int,input().split('.'))))
while generations:
    print('.'.join((str(i) for i in heapq.heappop(generations))))