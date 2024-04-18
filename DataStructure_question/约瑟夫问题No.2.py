from collections import deque
while True:
    n,p,m=map(int,input().split())
    res=[]
    if n==0:break
    q=deque(i for i in range(1,n+1))
    for _ in range(p - 1):
        tmp = q.popleft()
        q.append(tmp)
    while len(q)>0:
        for _ in range(m-1):
            tmp=q.popleft()
            q.append(tmp)
        res.append(str(q.popleft()))
    print(",".join(res))
