import heapq
def operate(l,s:str):
    if s[0]=='1':
        op,num=map(str,s.split())
        heapq.heappush(l,int(num))
    else:
        print(heapq.heappop(l))

l=[]
for _ in range(int(input())):
    operate(l,input())