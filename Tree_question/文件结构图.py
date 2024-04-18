class TreeNode:
    def __init__(self,val):
        self.val = val
        self.files = []
        self.dirs = []
        #留一个parent属性方便节点上移
        self.parent=None

# 根据输入数据建树，并返回根
def GraphTree(l:list):
    root=TreeNode('ROOT')
    current_node=root
    for name in l:
        if name[0]=='f':
            tmp=TreeNode(name)
            tmp.parent=current_node
            current_node.files.append(tmp)
        elif name[0]=='d':
            tmp=TreeNode(name)
            tmp.parent=current_node
            current_node.dirs.append(tmp)
            current_node=tmp
        else:
            # name=='[':
            current_node=current_node.parent
    return root

res=['ROOT']

# 递归绘图，根据根节点画出其下的文件以及目录
def DrawGraph(root:TreeNode,depth):
    # 函数的功能是把该根节点目录下的所有打印行添加到res中
    global res
    for dir in root.dirs:
        # 对于目录中的目录，同样执行该操作
        res.append("|     "*(depth+1)+dir.val)
        DrawGraph(dir,depth+1)

    root.files.sort(key=lambda x:x.val)
    for file in root.files:
        # 对于目录中的文件执行操作
        res.append('|     '*depth+file.val)
    return

# 简单处理一下数据
stack=[[]]
while (n:=input())!='#':
    if n!='*':stack[-1].append(n)
    else:stack.append([])
stack.pop()

for i in range(len(stack)):
    l,res=stack[i],['ROOT']
    root=GraphTree(l)
    DrawGraph(root,0)
    print('DATA SET {}:'.format(i+1))
    for j in res:
        print(j)
    if i!=len(stack)-1:
        print(" ")