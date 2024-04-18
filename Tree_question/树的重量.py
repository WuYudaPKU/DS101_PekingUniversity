res=0
def PutWeight(idx,weight):
    global n,k,tree
    if idx>=2**k:
        return
    tree[idx]+=weight
    PutWeight(idx*2,weight)
    PutWeight(idx*2+1,weight)

def GetWeight(idx):
    global res,tree,k
    if idx>=2**k:
        return
    res+=tree[idx]
    GetWeight(idx*2)
    GetWeight(idx*2+1)

k,n=map(int,input().split())
tree=[0 for _ in range(2**k)]

for _ in range(n):
    case=input()
    if case[0]=='1':
        op,idx,weight=map(int,case.split())
        PutWeight(idx,weight)
    else:
        op,idx=map(int,case.split())
        res=0
        GetWeight(idx)
        print(res)
