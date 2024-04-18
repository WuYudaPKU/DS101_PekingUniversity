from collections import defaultdict,deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def TreeBuilding(deq:deque):
    tree_slice=defaultdict(list)
    while deq:
        node=deq.popleft()
        node,name=node[:-1],node[-1]
        n=len(node)-1
        if n==-1:
            tree_slice[0].append(TreeNode(name))
        else:
            current_node=tree_slice[n][-1]
            to_be_append=TreeNode(name)
            if to_be_append.val=='*':
                if current_node.left==None:
                    current_node.left=TreeNode("")
                else:
                    current_node.right=TreeNode("")
            else:
                if current_node.left==None:
                    current_node.left=to_be_append
                else:
                    current_node.right=to_be_append
                tree_slice[n+1].append(to_be_append)

    # return root
    return tree_slice[0][0]

def pre_order(root):
    output=[]
    if root==None or root.val=="*":return output
    output.append(root.val)
    output.extend(pre_order(root.left))
    output.extend(pre_order(root.right))
    return "".join(output)

def in_order(root):
    output=[]
    if root==None or root.val=="*":return output
    output.extend(in_order(root.left))
    output.append(root.val)
    output.extend(in_order(root.right))
    return "".join(output)

def post_order(root):
    output=[]
    if root==None or root.val=="*":return output
    output.extend(post_order(root.left))
    output.extend(post_order(root.right))
    output.append(root.val)
    return "".join(output)

cases=int(input())
for i in range(cases):
    deq=deque()
    while (n:=input())!="0":
        deq.append(n)
    root=TreeBuilding(deq)
    print(pre_order(root)+"\n"+post_order(root)+"\n"+in_order(root)+"\n")