from collections import defaultdict,deque
class node_deque:
    def __init__(self,idx):
        self.idx=idx
        self.queue=deque()
# 多个映射，由队列索引映射到节点，以及由队员映射到索引
idx_to_node,member_to_idx,ans,q_seq={},defaultdict(int),[],deque()
t=int(input())

for i in range(t):
    idx_to_node[i+1]=node_deque(i+1)
    for member in map(int,input().split()):
        member_to_idx[member]=(i+1)

while (command:=input())!='STOP':
    if command[0]=='D':
        ans.append(idx_to_node[q_seq[0]].queue.popleft())
        if not idx_to_node[q_seq[0]].queue:q_seq.popleft()

    elif command[0]=='E':
        a,b=map(str,command.split())
        idx=member_to_idx[int(b)]
        if idx_to_node[idx].queue:
            idx_to_node[idx].queue.append(b)
        else:
            q_seq.append(idx)
            idx_to_node[idx].queue.append(b)

for i in ans:
    print(i)