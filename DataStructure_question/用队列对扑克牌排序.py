from collections import deque
n,pokes=int(input()),list(map(str,input().split()))
l_deque_1=[deque()]+[deque() for _ in range(9)]
l_deque_2=[deque()]+[deque() for _ in range(4)]
output,tmp=[],deque()
for poke in pokes:
    l_deque_1[int(poke[1])].append(poke)
for idx in range(1,len(l_deque_1)):
    output.append('Queue{}:'.format(idx)+' '.join(l_deque_1[idx]))

for idx in range(1,len(l_deque_1)):
    while l_deque_1[idx]:
        tmp.append(l_deque_1[idx].popleft())

for poke in tmp:
    if poke[0]=='A':
        l_deque_2[1].append(poke)
    elif poke[0]=='B':
        l_deque_2[2].append(poke)
    elif poke[0]=='C':
        l_deque_2[3].append(poke)
    else:
        l_deque_2[4].append(poke)

for idx in range(1,len(l_deque_2)):
    if idx==1:
        output.append('QueueA:'.format()+' '.join(l_deque_2[idx]))
    elif idx==2:
        output.append('QueueB:'.format()+' '.join(l_deque_2[idx]))
    elif idx==3:
        output.append('QueueC:'.format()+' '.join(l_deque_2[idx]))
    else:
        output.append('QueueD:'.format()+' '.join(l_deque_2[idx]))

tmp.clear()
for idx in range(1,len(l_deque_2)):
    while l_deque_2[idx]:
        tmp.append(l_deque_2[idx].popleft())
output.append(" ".join(tmp))
for i in output:
    print(i)