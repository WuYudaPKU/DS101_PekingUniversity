from collections import deque
n,a,b=map(int,input().split())
plants=deque(map(int,input().split()))
atmp,btmp,cnt=a,b,0
#len>3时奇偶操作相同
while len(plants)>=3:
    A=plants.popleft()
    B=plants.pop()
    if atmp<A:
        cnt+=1
        atmp=a
    if btmp<B:
        cnt+=1
        btmp=b
    atmp-=A
    btmp-=B

if len(plants)==1:
    if max(atmp,btmp)<plants.pop():
        cnt+=1
if len(plants)==2:
    A = plants.popleft()
    B = plants.pop()
    if atmp<A:
        cnt+=1
    if btmp<B:
        cnt+=1
print(cnt)