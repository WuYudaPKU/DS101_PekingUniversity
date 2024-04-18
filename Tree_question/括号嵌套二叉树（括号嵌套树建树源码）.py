class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children=[]

non_l=('(',')',',')
def BuildTree(s:str):
    # 该函数的作用是：通过s建树存到内存空间中，并返回根节点
    '''
    实现原理：
    发现字母即加入父节点的子列表中，子列表的正序即树从左到右；
    一个node循环指向某个实例，在遇见左括号时让这个实例入栈，
    并且在下一次最先弹出并且被当做父节点。
    遇见右括号则把栈顶元素弹出，意味着该节点的子树构建完成。
    '''
    stack=[]
    node=None
    for char in s:
        if char.isalpha():
            node=TreeNode(char)
            if stack:
                # 如果栈不为空，把节点作为子节点加入栈顶节点的子节点列表中
                stack[-1].children.append(node)
        elif char=='(':
            if node:
                stack.append(node)
                node=None
        elif char==')':
            if stack:
                node=stack.pop()
    return node

def pre_order(node):
    res=[node.value]
    for child in node.children:
        res.extend(pre_order(child))
    return ''.join(res)

def post_order(node):
    output=[]
    for child in node.children:
        output.extend(post_order(child))
    output.append(node.value)
    return ''.join(output)

def main():
    s = input().strip()
    s = ''.join(s.split())  # 去掉所有空白字符
    root = BuildTree(s)  # 解析整棵树
    if root:
        print(pre_order(root))  # 输出前序遍历序列
        print(post_order(root))  # 输出后序遍历序列
    else:
        print("input tree string error!")

if __name__ == "__main__":
    main()