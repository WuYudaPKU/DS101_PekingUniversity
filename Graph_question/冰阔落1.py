class DisjointSet:
    # 用index作为每个元素的储存位置。
    def __init__(self, n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0 for i in range(n+1)]

    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.parent[rootY]=rootX
            elif self.rank[rootX]<self.rank[rootY]:
                self.parent[rootX]=rootY
            else:
                self.parent[rootY]=rootX
                self.rank[rootX]+=1


while True:
    try:
        n,m=map(int,input().split())
        djs=DisjointSet(n)
        for _ in range(m):
            a,b=map(int,input().split())
            if djs.find(a)!=djs.find(b):
                djs.union(a,b)
                print('No')
            else:print('Yes')
        cnt,stack=0,[]
        for i in range(1,n+1):
            if djs.parent[i]==i:
                stack.append(i)
                cnt+=1
        print(cnt)
        print(*stack)
    except:break