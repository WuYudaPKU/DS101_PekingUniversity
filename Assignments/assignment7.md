# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

2024 spring, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/

思路：stack，感谢送分

代码

```python
raw=list(map(str,input().split()))
stack=[]
while raw:
    stack.append(raw.pop())
print(' '.join(stack))
```

代码运行截图 ==（至少包含有"Accepted"）==

![image-20240403174216621](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240403174216621.png)

### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/

思路：

代码

```python
from collections import deque
dic,dic_set,limit,cnt=deque(),set(),0,0
M,N=map(int,input().split())
passage=list(map(int,input().split()))

for i in passage:
    if limit<=M-1:
        if i in dic_set:continue
        else:
            cnt+=1
            limit+=1
            dic.append(i)
            dic_set.add(i)
    else:
        if i in dic_set:continue
        else:
            tmp=dic.popleft()
            dic_set.discard(tmp)
            dic.append(i)
            dic_set.add(i)
            cnt+=1
print(cnt)
```

代码运行截图 ==（至少包含有"Accepted"）==

![image-20240403174258973](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240403174258973.png)

### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：

代码

```python
n,k=map(int,input().split())
raw=list(map(int,input().split()))
raw.sort()
x=None
if k==0:
    if raw[0]==1:x=-1
    else:x=raw[0]-1

elif k>=1 and k<n:
    if raw[k]>raw[k-1]:
        x=raw[k-1]
    else:
        x=-1
else:x=raw[-1]

if x==-1:
    print(x)
elif x>=1 and x<=10**9:
    print(x)
else:
    print(-1)
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403174338797](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240403174338797.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/

思路：

和归并排序有相似之处。

由于这是一颗完美的二叉树，所以可以考虑从叶子结点向上建树。

代码

```python
"""我们可以把由 0 和 1 组成的字符串分为三类：全 0 串称为 B 串，全 1 串称为 I 串
既含 0 又含 1 的串则称为 F 串。
FBI 树是一种二叉树，它的结点类型也包括 F 结点，B 结点和 I 结点三种。"""
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

N=int(input())
raw=list(input())
ltype=[]
for i in raw:
    if i=='1':ltype.append(TreeNode('I'))
    else:ltype.append(TreeNode('B'))

def parent_type(type1,type2):
    if type1==type2=='I':
        return 'I'
    elif type1==type2=='B':
        return "B"
    else:return "F"

while len(ltype)>1:
    tmp=[]
    for i in range(0,len(ltype),2):
        left=ltype[i]
        right=ltype[i+1]
        parent=TreeNode(parent_type(left.val,right.val))
        parent.left=left
        parent.right=right
        tmp.append(parent)
    ltype=tmp

def post(node):
    output=[]
    if node==None:return output
    output.extend(post(node.left))
    output.extend(post(node.right))
    output.append(node.val)
    return "".join(output)

print(post(ltype[0]))
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403174503334](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240403174503334.png)

### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/

思路：

维护一个队列序s_seq，由队列序生成一个到队列的映射。

代码

```python
from collections import defaultdict,deque
class node_deque:
    def __init__(self,idx):
        self.idx=idx
        self.queue=deque()
# 多个映射，由队列索引映射到节点，以及由队员映射到索引
idx_to_node,member_to_idx,ans,q_seq={},defaultdict(int),[],deque()
t=int(input())

for i in range(t):
    idx_to_node[i+1]=node_deque(i+1)
    for member in map(int,input().split()):
        member_to_idx[member]=(i+1)

while (command:=input())!='STOP':
    if command[0]=='D':
        ans.append(idx_to_node[q_seq[0]].queue.popleft())
        if not idx_to_node[q_seq[0]].queue:q_seq.popleft()

    elif command[0]=='E':
        a,b=map(str,command.split())
        idx=member_to_idx[int(b)]
        if idx_to_node[idx].queue:
            idx_to_node[idx].queue.append(b)
        else:
            q_seq.append(idx)
            idx_to_node[idx].queue.append(b)

for i in ans:
    print(i)
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403174707447](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240403174707447.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/

思路：

代码

```python
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
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403174629914](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240403174629914.png)



## 2. 学习总结和收获

没睡醒，痛失半小时coding时间，差一道题AC6，这是离AC6最近的一次！

题目难度不大，模板性很强， 平时写习惯了很快就能AC。

学会了用pycharm debug以后上机快乐翻倍！半分钟内发现bug，大量节省时间。

笔试题目不熟悉，说明只学会了使用接口，内部实现理解的还不透彻，抓紧补上。





