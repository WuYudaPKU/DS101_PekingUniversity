class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.pairs=0

# 根据一个整理好的有序列表建树
def build_tree(l:list):
    global lst
    stack_1,stack_2=[],[]
    a=None
    for i in l:
        # 后面使用的number_buffer有点bug,会出现",这句是补丁
        if i=='':continue
        # 左括号入栈，继续
        if i=='(':
            stack_1.append(i)
            continue
        # 发现右括号，要收走一个左括号；如果数字栈栈顶元素累计被收走了两个左括号，则栈顶节点子树建完，将节点弹出
        # 这也是建立node.pairs属性的原因
        if i==')':
            stack_1.pop()
            if stack_2:
                stack_2[-1].pairs += 1
                if stack_2[-1].pairs==2:
                    a=stack_2.pop()
                    # 叶子结点存下来
                    if a.left==None and a.right==None:
                        lst.append(a)
            continue

        node=TreeNode(i)
        # 防止根节点找不到父节点
        if stack_2:
            if stack_1:
                # 如果栈顶节点已经建立完左子树，则新节点一定是其右儿子，否则左儿子。
                if stack_2[-1].pairs==1:
                    stack_2[-1].right=node
                    node.parent=stack_2[-1]
                    pass
                else:
                    stack_2[-1].left=node
                    node.parent=stack_2[-1]
        # 元素入数字栈
        stack_2.append(node)
    return a

# 前面所有叶子结点已经存在lst中，只需要从叶子结点向上遍历
def TreeSumming(node):
    if node.parent==None: return int(node.val)
    return int(node.val)+TreeSumming(node.parent)

# 将诸如['2','2','(']转化成['22','(']
def number_buffer(l:list):
    buffer,output=[],[]
    for i in l:
        if i in '()':
            output.append("".join(buffer))
            buffer.clear()
            output.append(i)
        else:
            buffer.append(i)
    return output

# 将混乱表达式解析地存入结果中
def parse_input(l:list):
    output,ans=[],[]
    for i in l:
        if not (i[0].isnumeric() or i[0]=='-'):
            output[-1]+=i
            continue
        output.append(i)
    output=[list(i) for i in output]

    for i in output:
        ans.append([j for j in i if (j!=" " and j!="")])
    ans=[number_buffer(i) for i in ans]
    return ans

raw=[]
while True:
    try:raw.append(input())
    except:break

standard_input=parse_input(raw)
for l in standard_input:
    lst=[]
    root=build_tree(l[1:])
    paths=[TreeSumming(node) for node in lst]
    print('yes' if int(l[0]) in paths else 'no')