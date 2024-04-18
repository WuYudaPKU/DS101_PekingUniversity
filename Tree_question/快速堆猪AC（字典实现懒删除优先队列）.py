import heapq
from collections import defaultdict
p_stack,p_heap,is_out=[],[],defaultdict(int)
while True:
    try:
        tmp=input()
        if tmp=="min":
            if p_stack:
                while True:
                    a=heapq.heappop(p_heap)
                    if not is_out[a]:
                        heapq.heappush(p_heap,a)
                        print(a)
                        break
                    else:
                        is_out[a]-=1
                        continue
        elif tmp=="pop":
            if p_stack:
                is_out[p_stack.pop()]+=1
        else:
            _,num=map(str,tmp.split())
            p_stack.append(int(num))
            heapq.heappush(p_heap,int(num))
    except EOFError:
        break