# Assignment #3: March月考

Updated 1537 GMT+8 March 6, 2024

2024 spring, Complied by 武昱达 23工院



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

Python编程环境：PyCharm 2023.3.4 (Professional Edition) & VSCode

操作系统：Windows 11

## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/

思路：

之前写过dp实现，由于数据量较小，这次使用dfs实现。

##### 代码

```python
# dfs
import math
k=int(input())
heights=list(map(int,input().split()))
res=0
def dfs(path,left):
    global res
    if len(left)==0:
        res=max(res,len(path))
        return
    if len(left)==1:
        height=left.pop()
        if height<path[-1]:
            path.append(height)
        res=max(len(path),res)
        return
    for i in range(len(left)):
        height=left[i]
        if height<=path[-1] or len(path)==0:
            dfs(path+[height],left[i+1:])
    return

dfs([math.inf],heights)
print(res-1)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240306221400540](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240306221400540.png)

**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147

思路：

递归。

##### 代码

```python
# 通过不断变化initiate，assistance和goal实现递归。
def OneMove(x,init,goal):
    print(str(x)+":"+init+"->"+goal)
def Move(num_disks,init,assist,goal):
    if num_disks == 1:
        OneMove(num_disks,init,goal)
    else:
        Move(num_disks-1,init,goal,assist)
        OneMove(num_disks,init,goal)
        Move(num_disks-1,assist,init,goal)

n,a,b,c=map(str,input().split())
Move(int(n),a,b,c)
```

代码运行截图 ==（至少包含有"Accepted"）==

![image-20240306221513119](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240306221513119.png)

**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253

思路：

简单的队列实现。

##### 代码

```python
# queue
from collections import deque
while True:
    n,p,m=map(int,input().split())
    res=[]
    if n==0:break
    q=deque(i for i in range(1,n+1))
    for _ in range(p - 1):
        tmp = q.popleft()
        q.append(tmp)
    while len(q)>0:
        for _ in range(m-1):
            tmp=q.popleft()
            q.append(tmp)
        res.append(str(q.popleft()))
    print(",".join(res))
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306221600224](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240306221600224.png)

**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554

思路：

很简单的贪心，用反证法可以轻松证明。

##### 代码

```python
# greedy
n,res,wait=int(input()),[],0
time=[0]+list(map(int,input().split()))
t_time=list((time[i],i) for i in range(1,n+1))
t_time.sort()
# print(t_time)
for i in range(n):
    res.append(t_time[i][1])
    wait+=t_time[i][0]*(n-1-i)
print(*res)
print('{:.2f}'.format(wait/n))
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306221647405](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240306221647405.png)

**19963:买学区房**

http://cs101.openjudge.cn/practice/19963

思路：

语法题，但是很烦。

##### 代码

```python
def mid_num(lst):
    tmp=sorted(lst)
    if len(lst)%2==0:
        return (tmp[len(lst)//2]+tmp[len(lst)//2-1])/2
    if len(lst)%2==1:
        return tmp[len(lst)//2]

n,res=int(input()),0
d_raw=list(map(str,input().split()))
d_1=[]

for i in range(n):
    a,b=map(str,d_raw[i].split(","))
    a,b=int(a[1:]),int(b[:len(b)-1])
    d_1.append((a,b))

p=list(map(int,input().split()))
d=[i+j for i,j in d_1]
p_mid=mid_num(p)
x=[]
for i in range(n):
    xt=d[i]/p[i]
    x.append(xt)
x_mid=mid_num(x)

for i,j in zip(x,p):
    if i>x_mid and j<p_mid:
        res+=1
print(res)
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306221728247](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240306221728247.png)

**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300

思路：

写一个排序函数，结合字典即可，defaultdict好用。

##### 代码

```python
def sort_str(scales):
    M_part,B_part=[],[]
    for i in scales:
        if i[-1]=="M":
            M_part.append(i)
        elif i[-1]=="B":
            B_part.append(i)
    B_part.sort(key=lambda x:float(x[:len(x)-1]))
    M_part.sort(key=lambda x:float(x[:len(x)-1]))
    return M_part+B_part

from collections import defaultdict
models=defaultdict(list)
for _ in range(n:=int(input())):
    name,scale=map(str,input().split("-"))
    models[name].append(scale)

lst=[]
for name,scales in models.items():
    lst.append((name,scales))
lst.sort(key=lambda x:x[0])
for name,scales in lst:
    print(name+": "+", ".join(sort_str(scales)))
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306221832313](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240306221832313.png)

## 2. 学习总结和收获

一直在跟进每日选做，目前要求自己每个题目都完成。

最近题目难度上来，不如前几天游刃有余，也是因为上学期每日选做做的很少（欠的债总是要还）。争取持续跟进。

目前仍然很难克服对递归的恐惧（同一函数体容易想不清楚、写不清楚），即使是简单的dfs不参考模版也写得很慢，仍然需要加强练习。汉诺塔问题没有写出来遗憾AC5.

快速堆猪学会了懒删除堆，非常好用。
