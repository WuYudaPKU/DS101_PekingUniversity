from collections import deque
dic,dic_set,limit,cnt=deque(),set(),0,0
M,N=map(int,input().split())
passage=list(map(int,input().split()))

for i in passage:
    if limit<=M-1:
        if i in dic_set:continue
        else:
            cnt+=1
            limit+=1
            dic.append(i)
            dic_set.add(i)
    else:
        if i in dic_set:continue
        else:
            tmp=dic.popleft()
            dic_set.discard(tmp)
            dic.append(i)
            dic_set.add(i)
            cnt+=1
print(cnt)