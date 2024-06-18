# Assignment #2: 编程练习

2024 spring, Complied by 23工院 武昱达

**编程环境**

操作系统：Windows 11

Python编程环境：pyCharm 2023.1.4 (Professional Edition)

## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/2024sp_routine/27653/

思路：

##### 代码

```python
import math
a1,a2,b1,b2=map(int,input().split())
temp1=a1*b2+b1*a2
temp2=a2*b2
a=math.gcd(temp1,temp2)
print(str(temp1//a)+"/"+str(temp2//a))
```

代码运行截图 ==（至少包含有"Accepted"）==

![image-20240224110537247](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240224110537247.png)

### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110

思路：

##### 代码

```python
n,w=map(int,input().split())
lst_candy=[]
for _ in range(n):
    lst_candy.append(list(map(int,input().split())))
for list_value_weight in lst_candy:
    value,weight=list_value_weight[0],list_value_weight[1]
    list_value_weight.append(value/weight)
lst_candy.sort(key=lambda x: x[2],reverse=True)
# print(lst_candy)
#lst_candy的格式为[[value,weight,value_per_weight],...]
weight=0
value=0
flag=0
while weight<w:
    try:
        if weight+lst_candy[flag][1]<w:
            value+=lst_candy[flag][0]
            weight+=lst_candy[flag][1]
            flag+=1

        else:
            left_weight=w-weight
            value+=lst_candy[flag][2]*left_weight
            break
    except:
        break
print(round(float(value),1))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240224110620959](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240224110620959.png)

### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

##### 代码

```python
nCases=int(input())
lst_1=[]
for _ in range(nCases):
    n,m,b=map(int,input().split())
    dict_raw={}
    set_ti=set()
    for i in range(n):
        ti,xi=map(int,input().split())
        set_ti.add(ti)
        try:
            temp=type(dict_raw[ti])
            dict_raw[ti].append(xi)
        except:
            dict_raw[ti]=[]
            dict_raw[ti].append(xi)
    # print(dict_raw)
    lst_ti=[i for i in set_ti]
    lst_ti.sort()
    # print(lst_ti)

    flag=0
    while True:
        try:
            if b>0:
                temp=dict_raw[lst_ti[flag]]
                temp.sort(reverse=True)
                times=0
                while times<m:
                    try:
                        b-=temp[times]
                        times+=1
                        if b<=0:
                            lst_1.append(lst_ti[flag])
                            break
                    except:
                        break
                flag+=1
            else:
                break
        except:
            break
    if b>0:
        lst_1.append("alive")
for i in lst_1:
    print(i)
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240224110701207](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240224110701207.png)

### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：判断完全平方数；欧拉筛

##### 代码

```python
import math
#判断是否为完全平方数 不是则pass（参考drunkjailor）
def is_perfect(x):
    sqrt=math.sqrt(x)
    if sqrt.is_integer():
        return True
    else:
        return False
#如果是完全平方数，判断因子个数
def Euler_sieve(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return primes
tuple_primes=tuple(Euler_sieve(1000000))
def is_T_primes(x):
    set_1=set()
    if not is_perfect(x):
        return False
    if x==4 or x==9:
        return True
    elif x==1:
        return False
    else:
        a=int(math.sqrt(x))
        tuple_basic=(0,2,3,4)
        if a%6 in tuple_basic:
            return False
        else:
            if tuple_primes[a]:
                return True
            else:
                return False
 
 
n=int(input())
int_tuple=tuple(map(int,input().split()))
int_set=set(int_tuple)
dict_1={i:is_T_primes(i) for i in int_set}
for i in int_tuple:
        print("YES" if dict_1[i] else "NO")
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240224110813970](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240224110813970.png)

### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A

思路：

##### 代码

```python
def prefix_sum(nums):
    prefix = []
    total = 0
    for num in nums:
        total += num
        prefix.append(total)
    return prefix

def suffix_sum(nums):
    suffix = []
    total = 0
    # 首先将列表反转
    reversed_nums = nums[::-1]
    for num in reversed_nums:
        total += num
        suffix.append(total)
    # 将结果反转回来
    suffix.reverse()
    return suffix


t = int(input())
for _ in range(t):
    N, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    aprefix_sum = prefix_sum(a)
    asuffix_sum = suffix_sum(a)

    left = 0
    right = N - 1
    if right == 0:
        if a[0] % x !=0:
            print(1)
        else:
            print(-1)
        continue

    leftmax = 0
    rightmax = 0
    while left != right:
        total = asuffix_sum[left]
        if total % x != 0:
            leftmax = right - left + 1
            break
        else:
            left += 1

    left = 0
    right = N - 1
    while left != right:
        total = aprefix_sum[right]
        if total % x != 0:
            rightmax = right - left + 1
            break
        else:
            right -= 1

    if leftmax == 0 and rightmax == 0:
        print(-1)
    else:
        print(max(leftmax, rightmax))

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240224110915412](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240224110915412.png)

### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/

思路：

##### 代码

```python
import math
def is_perfect(x):
    sqrt = math.sqrt(x)
    if sqrt.is_integer():return True
    else:return False
def Euler_sieve(n):
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes
tuple_primes = tuple(Euler_sieve(10000))
def is_T_primes(x):
    set_1 = set()
    if not is_perfect(x):
        return False
    if x == 4 or x == 9:return True
    elif x == 1:return False
    else:
        a = int(math.sqrt(x))
        tuple_basic = (0, 2, 3, 4)
        if a % 6 in tuple_basic:return False
        else:
            if tuple_primes[a]:return True
            else:return False

m,n=map(int,input().split())
res=[]
for i in range(m):
    temp=list(map(int,input().split()))
    valid=[]
    for j in temp:
        if is_T_primes(j):
            valid.append(j)
    if valid:res.append("{:.2f}".format(sum(valid)/len(temp)))
    else:res.append(0)

for i in res:
    print(i)
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240224112342557](C:\Users\86178\AppData\Roaming\Typora\typora-user-images\image-20240224112342557.png)

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

题目都做过，非常简单；额外完成了一些有关树的题目。





