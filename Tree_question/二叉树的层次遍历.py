from collections import deque

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def Parse_tree(s:deque):
    l=len(s)
    stack = []
    node_dict=dict()
    while s:
        name=s.popleft()
        node_dict[name]=TreeNode(name)
        if name.islower():
            stack.append(node_dict[name])
        else:
            num_2=stack.pop()
            num_1=stack.pop()
            node_dict[name].left=num_1
            node_dict[name].right=num_2
            stack.append(node_dict[name])
    root=stack[0]
    res=Tree_BFS(root,l)
    return res

# 用BFS的方法遍历二叉树
def Tree_BFS(root,l):
    queue=deque()
    queue.append(root)
    res=[root.value]
    while len(res)<l:
        a=queue.popleft()
        if a.left!=None:
            res.append(a.left.value)
            queue.append(a.left)
        if a.right!=None:
            res.append(a.right.value)
            queue.append(a.right)
    return res

for _ in range(int(input())):
    raw=deque(input())
    print("".join(reversed(Parse_tree(raw))))