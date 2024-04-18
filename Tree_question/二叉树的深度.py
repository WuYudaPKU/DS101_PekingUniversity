class TreeNode:
    def __init__(self):
        self.left=None
        self.right=None
        self.parent=None
def TreeHeight(root):
    if root==None:
        return 0
    return max(TreeHeight(root.left),TreeHeight(root.right))+1

n=int(input())
nodes=[TreeNode() for _ in range(n)]

for node in range(n):
    left,right=map(int,input().split())
    if left!=-1:
        nodes[left-1].parent=nodes[node]
        nodes[node].left=nodes[left-1]
    if right!= -1:
        nodes[node].right=nodes[right-1]
        nodes[right-1].parent=nodes[node]
root=None
for node in nodes:
    if node.parent==None:
        root=node
        break
print(TreeHeight(root))