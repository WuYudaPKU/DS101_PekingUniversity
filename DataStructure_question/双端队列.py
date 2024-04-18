from collections import deque
for _ in range(t:=int(input())):
    q=deque()
    for _ in range(n:=int(input())):
        type,num=map(int,input().split())
        if type==1:
            q.append(num)
        else:
            if num==0:
                q.popleft()
            else:
                q.pop()
    if q:
        print(*q)
    else:
        print("NULL")


