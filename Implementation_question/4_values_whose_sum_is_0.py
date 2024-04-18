import itertools
A,B,C,D=[],[],[],[]
n,res=int(input()),0
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for tup in itertools.product(A,B,C,D):
    if sum(tup)==0:res+=1
print(res)