"""我们可以把由 0 和 1 组成的字符串分为三类：全 0 串称为 B 串，全 1 串称为 I 串
既含 0 又含 1 的串则称为 F 串。
FBI 树是一种二叉树，它的结点类型也包括 F 结点，B 结点和 I 结点三种。"""
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

N=int(input())
raw=list(input())
ltype=[]
for i in raw:
    if i=='1':ltype.append(TreeNode('I'))
    else:ltype.append(TreeNode('B'))

def parent_type(type1,type2):
    if type1==type2=='I':
        return 'I'
    elif type1==type2=='B':
        return "B"
    else:return "F"

while len(ltype)>1:
    tmp=[]
    for i in range(0,len(ltype),2):
        left=ltype[i]
        right=ltype[i+1]
        parent=TreeNode(parent_type(left.val,right.val))
        parent.left=left
        parent.right=right
        tmp.append(parent)
    ltype=tmp

def post(node):
    output=[]
    if node==None:return output
    output.extend(post(node.left))
    output.extend(post(node.right))
    output.append(node.val)
    return "".join(output)

print(post(ltype[0]))