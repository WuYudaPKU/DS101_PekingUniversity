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