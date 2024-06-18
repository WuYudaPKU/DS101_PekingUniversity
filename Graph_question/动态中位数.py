import heapq
class Medium_finder:
    def __init__(self):
        self.big_heap=[]
        self.small_heap=[]
        self.big_size=0
        self.small_size=0

    def insert(self,val):
        if self.big_size-self.small_size==1:
            heapq.heappush(self.small_heap,val)
            self.small_size+=1
        elif self.big_size==self.small_size:
            heapq.heappush(self.big_heap,-val)
            self.big_size+=1
        if not self.big_heap or not self.small_heap:return
        while -self.big_heap[0] > self.small_heap[0]:
            big=-heapq.heappop(self.big_heap)
            small=heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap,-small)
            heapq.heappush(self.small_heap,big)

    def findMedium(self):
        if self.big_size==self.small_size:
            return (self.small_heap[0]-self.big_heap[0])/2
        if self.big_size>self.small_size:
            return -self.big_heap[0]

for _ in range(n:=int(input())):
    raw=list(map(int,input().split()))
    m_finder=Medium_finder()
    res=[]
    for idx,val in enumerate(raw):
        m_finder.insert(val)
        if (idx+1)%2==1:
            res.append(m_finder.findMedium())
    print(len(res))
    print(*res)