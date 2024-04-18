class TreeNode:
    def __init__(self,val):
        self.val=val
        self.children=[]
        self.parent=None

def get_val(node:TreeNode):
    tmp=[]
    output=[]
    if node==None:return output
    if not node.children:return [node.val]

    tmp.append(node)
    tmp.extend(node.children)
    tmp.sort(key=lambda x:x.val)

    for son in tmp:
        if son==node:
            output.append(son.val)
        else:
            output.extend(get_val(son))
    return output

n=int(input())
tree_dict={}
for i in range(n):
    a=input()
    if len(a)==1:
        try:
            tmp=tree_dict[int(a)]
        except:
            tmp=TreeNode(int(a))
            tree_dict[int(a)]=tmp
    else:
        lst=list(map(int,a.split()))
        val=lst[0]
        try:tmp=tree_dict[val]
        except:tree_dict[val]=TreeNode(val)

        for i in lst[1:]:
            try:tree_dict[i].parent=tree_dict[val]
            except:
                tree_dict[i]=TreeNode(i)
                tree_dict[i].parent = tree_dict[val]

        tree_dict[val].children.extend(tree_dict[i] for i in lst[1:])


root=None
for node in tree_dict.values():
    if node.parent==None:
        root=node
        break
for i in get_val(root):
    print(i)