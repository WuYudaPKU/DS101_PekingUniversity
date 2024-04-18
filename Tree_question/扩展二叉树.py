from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.parent=None

def fill_tree(root,node):
    node.parent=root
    if root.left==None:root.left=node
    else:root.right=node

# 函数的功能是建成以root为根的树，并把他连接到parent节点上。
def build_tree(d:deque,parent:TreeNode):
    if not d:return
    cur_node=TreeNode(d.popleft())

    while parent.left and parent.right:
        parent=parent.parent
    cur_node.parent=parent
    fill_tree(parent,cur_node)

    if cur_node.val=='.':
        build_tree(d,parent)
    else:build_tree(d,cur_node)

def post_search(root):
    if root.val == '.':
        return ""
    output=[]
    output.extend(post_search(root.left))
    output.extend(post_search(root.right))
    output.append(root.val)
    return "".join(output)

def in_search(root):
    if root.val=='.':
        return ""
    output=[]
    output.extend(in_search(root.left))
    output.append(root.val)
    output.extend(in_search(root.right))
    return "".join(output)

raw=deque(input())
root=TreeNode(raw.popleft())
build_tree(raw,root)
print(in_search(root))
print(post_search(root))