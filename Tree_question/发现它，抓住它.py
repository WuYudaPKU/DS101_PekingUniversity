class ZeroOneTreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.parent=self
    def find_root(self,flag=True):
        if self.parent==self:return self,flag

        if self==self.parent.left:
            return self.parent.find_root(flag)
        else:
            return self.parent.find_root(not flag)

class ZeroOneTree:
    def __init__(self,root:ZeroOneTreeNode):
        self.root=root

    # 定义同义节点：如果某节点与根节点属于相同集合，则称二者互为同义节点
    # 将节点插入最近的同义节点的右侧，或反义节点的左侧
    def _insert(self,current_node,same,node_to_add):
        if same and not current_node.right:
            current_node.right=node_to_add
            return
        if (not same) and not current_node.left:
            current_node.left=node_to_add
            return
        self._insert(current_node.left,same,node_to_add)

    # union的功能是，把node2节点的祖先定义为根，并且
    def union(self,node1:ZeroOneTreeNode,node2:ZeroOneTreeNode):
        if node1.find_root()[0]==self.root:
            if node1.parent.left==None:
                node1.parent.left=node2
            else:self._insert(node1,True,node2)


    def in_one(self,node1,node2):
        root1,judge1=node1.find_root()
        root2,judge2=node2.find_root()
        if root1==root2:
            if judge1==judge2:return "In the same gang."
            else:return 'In different gangs.'
        else:return 'Not sure yet.'