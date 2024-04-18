from collections import defaultdict,deque
class TreeNode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

existed=defaultdict(int)
#insert函数的功能是返回一个可以插入key的地址

def insert(root,key,parent_root,is_right):
    # root是当前正在进行操作的节点，parent_root是其父节点

    # 边界条件
    if root==None and is_right==True:
        parent_root.right=TreeNode(key)
        return
    elif root==None and is_right==False:
        parent_root.left=TreeNode(key)
        return

    #递归部分，把key插入右子树或左子树
    if int(key)>int(root.val):
        insert(root.right,key,root,is_right=True)
    else:
        insert(root.left,key,root,is_right=False)


def Tree_BFS(root,l):
    queue=deque()
    queue.append(root)
    res=[root.val]
    while len(res)<l:
        a=queue.popleft()
        if a.left!=None:
            res.append(a.left.val)
            queue.append(a.left)
        if a.right!=None:
            res.append(a.right.val)
            queue.append(a.right)
    return res

raw=list(map(str,input().split()))
root=TreeNode(raw[0])
existed[raw[0]]=True
cnt=1
for i in raw[1:]:
    if not existed[i]:
        insert(root,i,None,True)
        cnt+=1
    existed[i]=1

print(" ".join(Tree_BFS(root,cnt)))

# 51 45 59 86 45 4 15 76 60 20 61 77 62 30 2 37 13 82 19 74 2 79 79 97 33 90 11 7 29 14 50 1 96 59 91 39 34 6 72 7