from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#初始化global变量
node_dict,post_order,idx,current_node=dict(),[],0,None

# 函数的功能是建立起以name为根的子树，参数是name和中序表达式
def TreeBuilding(name,in_order:list):
    # idx全局变量寻找右子树根
    # current_node指向现在操作的对象
    global idx,current_node,node_dict,post_order
    #设置递归出口
    if len(in_order)==1:
        node_dict[name]=TreeNode(name)
        if current_node.right==None:
            current_node.right=node_dict[name]
            return
        current_node.left=node_dict[name]
        return

    # 建立树根并存在字典中，便于索引
    node_dict[name]=TreeNode(name)

    # 如果name节点是一个子节点，那current_node!=None
    # 建立起name和current_node的连接。
    if current_node!=None:
        if current_node.right==None:
            current_node.right=node_dict[name]
            pass
        elif current_node.left==None:
            current_node.left=node_dict[name]

    # 标明现在状态
    current_node=node_dict[name]
    pivot=in_order.index(name)

    # 建立右子树
    rtree_in_order=in_order[pivot+1:]
    if rtree_in_order:
        idx-=1
        TreeBuilding(post_order[idx],rtree_in_order)

    # 建立左子树
    current_node=node_dict[name]
    ltree_in_order=in_order[:pivot]
    if ltree_in_order:
        idx-=1
        TreeBuilding(post_order[idx],ltree_in_order)

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

n=int(input())
for i in range(n):
    node_dict=dict()
    in_order=list(input())
    post_order=list(input())
    # 最初的父节点指向None，即根节点的父节点指向None
    current_node=None
    idx=len(post_order)-1
    if len(post_order)==1:
        print(post_order[0])
    else:
        TreeBuilding(post_order[idx], in_order)
        print("".join(Tree_BFS(node_dict[post_order[-1]],len(post_order))))