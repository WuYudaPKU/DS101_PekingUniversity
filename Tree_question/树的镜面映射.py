from collections import deque
class GenericTreeNode:
    def __init__(self,val):
        self.val=val
        self.children=[]

def build_tree(tempList,index):
    node=GenericTreeNode(tempList[index][0])

    if tempList[index][1]=='0' and node.val!='$':
        index+=1
        child,index=build_tree(tempList,index)
        node.children.append(child)
        index+=1
        child,index=build_tree(tempList,index)
        node.children.append(child)

    return node,index

def print_tree(p):
    Q,S=deque(),deque()
    while p!=None:
        if p.val!='$':
            S.append(p)
        p=p.children[1] if len(p.children)>1 else None

    while S:
        Q.append(S.pop())
    while Q:
        p=Q.popleft()
        print(p.val,end=' ')

        if p.children:
            p=p.children[0]
            while p!=None:
                if p.val!="$":
                    S.append(p)
                p=p.children[1] if len(p.children)>1 else None

            while S:
                Q.append(S.pop())

n=int(input())
tempList=input().split()
root,_=build_tree(tempList,0)
print_tree(root)