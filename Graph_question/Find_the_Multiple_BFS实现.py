from collections import deque
def find_the_Multiple_BFS(n):
    queue = deque()
    _01=['0','1']
    queue.extend(_01)
    while True:
        tmp=queue.popleft()
        if int(tmp)==0:continue
        if int(tmp)%n==0:return int(tmp)

        queue.append(tmp+'0')
        queue.append(tmp+'1')

while (m:=int(input()))!=0:
    print(find_the_Multiple_BFS(m))