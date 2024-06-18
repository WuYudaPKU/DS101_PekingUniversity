from collections import deque
import copy
class Pot:
    def __init__(self,vol):
        self.vol=vol
        self.contains=0
    def fill(self):
        self.contains=self.vol

    def drop(self):
        self.contains=0

    def pour_into(self,other):
        to_pour=self.contains
        space=other.vol-other.contains
        if to_pour<=space:
            other.contains+=self.contains
            self.contains=0
        else:
            other.contains=other.vol
            self.contains-=space

class Stage:
    def __init__(self,pot1:Pot,pot2:Pot,previous_stage=None,previous_op=None):
        self.pot1=pot1
        self.pot2=pot2
        self.pot1_contains=pot1.contains
        self.pot2_contains=pot2.contains
        self.previous_op=previous_op
        self.previous_stage=previous_stage
        self.re=(self.pot1_contains,self.pot2_contains)

    def __str__(self):
        return str(self.pot1_contains)+" "+str(self.pot2_contains)

def traverse(stage):
    stack=[]
    while stage.previous_stage!=None:
        stack.append(stage.previous_op)
        stage=stage.previous_stage
    return reversed(stack)

visited=set()
def BFS(pot1:Pot,pot2:Pot,goal):
    operations=[i for i in range(1,7)]
    dq=deque()
    start_stage=Stage(pot1,pot2)
    dq.append(start_stage)

    while dq:
        stage=dq.popleft()
        if stage.re in visited:continue
        visited.add(stage.re)
        if stage.pot1_contains==goal or stage.pot2_contains==goal:
            return traverse(stage)
        else:
            for i in operations:
                if i==1:
                    stage.pot1.fill()
                    tmp=Stage(copy.deepcopy(pot1),copy.deepcopy(pot2),stage,i)
                    if tmp.re not in visited:
                        dq.append(tmp)
                elif i==2:
                    stage.pot1.drop()
                    tmp=Stage(copy.deepcopy(pot1),copy.deepcopy(pot2),stage,i)
                    if tmp.re not in visited:
                        dq.append(tmp)
                elif i==3:
                    stage.pot1.pour_into(pot2)
                    tmp=Stage(copy.deepcopy(pot1),copy.deepcopy(pot2),stage,i)
                    if tmp.re not in visited:
                        dq.append(tmp)
                elif i==4:
                    stage.pot2.fill()
                    tmp=Stage(copy.deepcopy(pot1),copy.deepcopy(pot2),stage,i)
                    if tmp.re not in visited:
                      dq.append(tmp)
                elif i==5:
                    stage.pot2.drop()
                    tmp=Stage(copy.deepcopy(pot1),copy.deepcopy(pot2),stage,i)
                    if tmp.re not in visited:
                        dq.append(tmp)
                elif i==6:
                    stage.pot2.pour_into(pot1)
                    tmp=Stage(copy.deepcopy(pot1),copy.deepcopy(pot2),stage,i)
                    if tmp.re not in visited:
                        dq.append(tmp)

Vol1,Vol2,goal=map(int,input().split())
pot1,pot_2=Pot(Vol1),Pot(Vol2)
print(BFS(pot1,pot_2,goal))