import heapq
class PigStack:
    def __init__(self):
        self.stack=[]
        self.heap=[]

    def push(self,element):
        self.stack.append(element)
        heapq.heappush(self.heap,element)

    def min(self):
        a=heapq.heappop(self.heap)
        heapq.heappush(self.heap,a)
        return a
    
    def pop(self):
        tmp=self.stack.pop()
        while True:
            tmp_lst=[]
            a=heapq.heappop(self.heap)
            if a==tmp:
                break
            tmp_lst.append(a)
        for i in tmp_lst:
            heapq.heappush(self.heap,i)

p=PigStack()
while True:
    try:
        tmp=input()
        if tmp=="pop":
            if p.stack:
                p.pop()
        elif tmp=="min":
            if p.stack:
                print(p.min())
        else:
            _,num=map(str,tmp.split())
            p.push(num)
    except EOFError:
        break