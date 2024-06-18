class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.parent=None

    def is_left_to(self,parent):
        return parent.left==self

    def _exchange_parent(self,other):
        self.parent,other.parent=other.parent,self.parent
        return other.parent,self.parent

    def exchange(self,other):
        parent_1,parent_2=self._exchange_parent(other)
        flag_1,flag_2=None,None

        if self.is_left_to(parent_1):flag_1=True
        else:flag_1=False

        if other.is_left_to(parent_2):flag_2=True
        else:flag_2=False

        if flag_1:parent_1.left = other
        else:parent_1.right=other

        if flag_2:parent_2.left=self
        else:parent_2.right=self

    def find_left_most(self):
        if self.left==None:return self
        return self.left.find_left_most()
for _ in range(t:=int(input())):
    n,m=map(int,input().split())
    tree={}

    for _ in range(n):
        val,left,right=map(int,input().split())
        if val not in tree:tree[val]=TreeNode(val)
        if left not in tree:tree[left]=TreeNode(left)
        if right not in tree:tree[right]=TreeNode(right)
        if left!=-1:
            tree[val].left=tree[left]
            tree[left].parent=tree[val]
        if right!=-1:
            tree[val].right=tree[right]
            tree[right].parent=tree[val]

    for _ in range(m):
        if (raw:=input())[0]=='1':
            type,x,y=map(int,raw.split())
            tree[x].exchange(tree[y])
        else:
            type,val=map(int,raw.split())
            print(tree[val].find_left_most().val)