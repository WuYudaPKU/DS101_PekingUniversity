import itertools
from collections import defaultdict
A,B,C,D=[],[],[],[]
n,res=int(input()),0
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

res=0
sum_1=defaultdict(int)
for i in itertools.product(A,B):
    sum_1[sum(i)]+=1

for i in range(n):
    for j in range(n):
        sum_2=C[i]+D[j]
        if sum_1[-sum_2]:
            res+=sum_1[-sum_2]
print(res)