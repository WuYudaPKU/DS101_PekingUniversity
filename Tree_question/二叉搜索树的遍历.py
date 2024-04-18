class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def Preorder_Buildtree(l:list,current_root):
    if len(l)==1:
        return current_root
    right_start=None
    for i in range(1,len(l)):
        if l[i]>current_root.val:
            right_start=i
            break
    if right_start==1:
        right=TreeNode(l[1])
        current_root.right=Preorder_Buildtree(l[1:],right)
    else:
        left=TreeNode(l[1])
        current_root.left=Preorder_Buildtree(l[1:right_start],left)
        if right_start:
            right=TreeNode(l[right_start])
            current_root.right=Preorder_Buildtree(l[right_start:],right)
    return current_root

def post_order(root):
    output=[]
    if root==None:
        return output
    output.extend(post_order(root.left))
    output.extend(post_order(root.right))
    output.append(root.val)
    return output

n,lst=int(input()),list(map(int,input().split()))
root=TreeNode(lst[0])
Preorder_Buildtree(lst,root)
print(*post_order(root))