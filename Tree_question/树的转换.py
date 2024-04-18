# for a generic_tree,we make its left son as its left son
# and make its right brother its right son, then a generic
# tree is shifted to a binary tree.
'''
    0                             0
  / | \                          /
 1  2  3       ===>             1
   / \                           \
  4   5                           2
                                 / \
                                4   3
                                 \
                                  5
'''
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children=[]
        self.parent=None
        self.bro=None
        self.left=None
        self.right=None
    def get_max_H(self):
        if not self.children:return 1
        return max(child.get_max_H() for child in self.children)+1
    def get_new_max_h(self):
        if self.left==None and self.right==None:
            return 1
        if self.left==None and self.right:
            return self.right.get_new_max_h()+1
        if self.right==None and self.left:
            return self.left.get_new_max_h()+1
        if self.left and self.right:
            return max(self.left.get_new_max_h(),self.right.get_new_max_h())+1

num=0
def build_generic_tree(l:list,current_node):
    global num
    if len(l)==0:
        return
    if l[0]=="d":
        num += 1
        node = TreeNode(num)
        if current_node.children:
            current_node.children[-1].bro=node
        current_node.children.append(node)
        node.parent=current_node
        build_generic_tree(l[1:],node)
    if l[0]=='u':
        build_generic_tree(l[1:],current_node.parent)
    return current_node

def build_new_tree(root,last_root,is_left:bool):
    new_root=TreeNode(root.value)
    if last_root:
        if is_left:last_root.left=new_root
        else:last_root.right=new_root

    if root.children:
        build_new_tree(root.children[0],new_root,True)
    if root.bro:
        build_new_tree(root.bro,new_root,False)
    return new_root


root=TreeNode(0)
build_generic_tree(list(input()),root)
new_root=build_new_tree(root,None,False)
print('{} => {}'.format(root.get_max_H()-1,new_root.get_new_max_h()-1))