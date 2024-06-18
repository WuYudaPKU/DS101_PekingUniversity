# Assignment #1: 拉齐大家Python水平

2024 spring, Complied by 23工院 武昱达

**编程环境**

操作系统：Windows 11

Python编程环境：PyCharm 2023.1.4 (Professional Edition)

## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/

思路：

带@lru_cache的动态规划

##### 代码

```python
# 23工院 武昱达
from functools import lru_cache
@lru_cache(maxsize=None)
def T(n):
    if n==0:return 0
    if n==1:return 1
    if n==2:return 1
    return T(n-3)+T(n-2)+T(n-1)

print(T(int(input())))
```

代码运行截图 ==（至少包含有"Accepted"）==

![image-20240222131902374](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240222131902374.png)

### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A

思路：

见注释

##### 代码

```python
# 23工院 武昱达
list_s = list(input())
list_result = []
list_hello=list("hello")
judge = 1
for index,item in enumerate(list_hello): #对每一个字母进行遍历
    try: #防止索引超出范围
        while item != list_s[index]:  #当第index个索引不是对应字母时，将字母删除
            try:
                list_s.remove(list_s[index])
            except IndexError: #删到出现错误，说明输入不合要求
                judge=0
                break
    except IndexError:#索引出现错误，说明输入不合要求
        judge=0

if len(list_s) <5:
    judge = 0
else:
    for i in range(5):
        list_result.append(list_s[i])

if "".join(list_result)=="hello":
    judge = 1

if judge == 0:
    print("NO")
elif judge==1:
    print("YES")
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240222132055815](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240222132055815.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A

思路：

##### 代码

```python
# 23工院 武昱达
dict_vowel = ['A','O','Y','E','U','I',
              'a','o','y','e','u','i']
word=input()
list_word=list(word)
list_result=[]
for index,item in enumerate(list_word):
    if item not in dict_vowel:
        list_result.append(item.lower())
for index,item in enumerate(list_result):
     list_result[index] = "."+item
print("".join(list_result))
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240222132221747](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240222132221747.png)

### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：

欧拉筛

##### 代码

```python
# 23工院 武昱达
def Euler_sieve(n):
    primes = [False]+[True for _ in range(n)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return primes

n=int(input())
l=Euler_sieve(10000)
for i in range(n//2):
    if l[i] and l[n-i]:
        print(i,n-i)
        break
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240222132659039](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240222132659039.png)

### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/

思路：

##### 代码

```python
raw=list(map(str,input().split("+")))
res=0
for i in raw:
    a,b=map(str,i.split("^"))
    if a[0]!="0":
        res=max(res,int(b))
print("n^"+str(res))
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240222132804900](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240222132804900.png)

### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/

思路：

##### 代码

```python
# 23工院 武昱达
from collections import defaultdict
raw=list(map(int,input().split()))
votes=defaultdict(int)
for i in raw:
    votes[i]+=1

temp=[(i,j) for i,j in votes.items()]
temp.sort(key=lambda x:x[1],reverse=True)

out=[]
for i in temp:
    if i[1]==max(votes.values()):
        out.append(i[0])
    else:
        break
out.sort()
print(*out)
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240222133734342](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240222133734342.png)

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“数算pre每日选做”、CF、LeetCode、洛谷等网站题目。==

题目比较简单，适合作为恢复训练。
