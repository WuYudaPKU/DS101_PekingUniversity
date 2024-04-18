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