from collections import deque,defaultdict
N=int(input())
l=[-1 for _ in range(N+1)]
r=[-1 for _ in range(N+1)]
for i in range(1,N+1):
    left,right=map(int,input().split())
    l[i],r[i]=left,right

def BFS(root):
    q,step=deque(),0
    q.append((root,step))
    buffer,ans=defaultdict(list),[]

    while q:
        cur,step=q.popleft()
        buffer[step].append(cur)
        if l[cur]!=-1:q.append((l[cur],step+1))
        if r[cur]!=-1:q.append((r[cur],step+1))

    for step in buffer:
        ans.append(buffer[step][-1])
    return ans

ans=BFS(1)
print(*ans)