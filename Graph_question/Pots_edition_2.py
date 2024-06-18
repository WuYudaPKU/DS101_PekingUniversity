from collections import deque
Vol1,Vol2,goal=map(int,input().split())
def fill(contain1,contain2,i):
    global Vol1,Vol2,goal
    if i==1:contain1=Vol1
    else:contain2=Vol2
    return (contain1,contain2)

def drop(contain1,contain2,i):
    global Vol1, Vol2, goal
    if i==1:contain1=0
    else:contain2=0
    return (contain1,contain2)

def no_order_pour(f,t,tvol):
    to_pour=f
    space=tvol-t
    if to_pour>space:
        tleft=to_pour-space
        return (tleft,tvol)
    else:
        return (0,t+to_pour)

def pour(contain1,contain2,i):
    # from contains1 to contains2
    global Vol1, Vol2, goal
    if i==1:
        contains1,contains2=no_order_pour(contain1,contain2,Vol2)
        return (contains1,contains2)
    elif i==2:
        contains2,contains1=no_order_pour(contain2,contain1,Vol1)
        return (contains1,contains2)

class Stage:
    def __init__(self,contains1,contains2,previous_stage=None,previous_op=None):
        self.contains1=contains1
        self.contains2=contains2
        self.previous_stage=previous_stage
        self.previous_op=previous_op

    def __str__(self):
        return str(self.contains1)+" "+str(self.contains2)

def traverse(stage):
    stack=[]
    while stage.previous_stage!=None:
        stack.append(stage.previous_op)
        stage=stage.previous_stage
    stack.reverse()
    return stack

def BFS(vol1,vol2,goal):
    dq=deque()
    visited=set()
    stage0=Stage(0,0)
    dq.append(stage0)
    while dq:
        cur_stage=dq.popleft()
        contains1=cur_stage.contains1
        contains2=cur_stage.contains2
        if contains1==goal or contains2==goal:return traverse(cur_stage)

        test=(contains1,contains2)
        if test in visited:continue
        visited.add(test)

        for i in range(6):
            if i==0:
                ncontains1,ncontains2=fill(contains1,contains2,1)
                new_stage=Stage(ncontains1,ncontains2,cur_stage,i)
                if (ncontains1,ncontains2) not in visited:
                    dq.append(new_stage)
            elif i==1:
                ncontains1,ncontains2=drop(contains1,contains2,1)
                new_stage=Stage(ncontains1,ncontains2,cur_stage,i)
                if (ncontains1, ncontains2) not in visited:
                    dq.append(new_stage)
            elif i==2:
                ncontains1,ncontains2=pour(contains1,contains2,1)
                new_stage=Stage(ncontains1,ncontains2,cur_stage,i)
                if (ncontains1, ncontains2) not in visited:
                    dq.append(new_stage)
            elif i==3:
                ncontains1,ncontains2=fill(contains1,contains2,2)
                new_stage=Stage(ncontains1,ncontains2,cur_stage,i)
                if (ncontains1, ncontains2) not in visited:
                    dq.append(new_stage)
            elif i==4:
                ncontains1,ncontains2=drop(contains1,contains2,2)
                new_stage=Stage(ncontains1,ncontains2,cur_stage,i)
                if (ncontains1, ncontains2) not in visited:
                    dq.append(new_stage)
            elif i==5:
                ncontains1,ncontains2=pour(contains2,contains1,2)
                new_stage=Stage(ncontains1,ncontains2,cur_stage,i)
                if (ncontains1, ncontains2) not in visited:
                    dq.append(new_stage)

res=BFS(Vol1,Vol2,goal)
op={}
op[1]='FILL(1)'
op[2]='DROP(1)'
op[3]='POUR(1,2)'
op[4]='FILL(2)'
op[5]='DROP(2)'
op[6]='POUR(2,1)'

print(len(res))
for i in res:print(op[i])