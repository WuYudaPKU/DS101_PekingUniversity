class DisjointSet:
    # 实际上是用index作为每个元素的储存位置。
    def __init__(self, n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0 for _ in range(n+1)]

    def find(self, x):  # find方法的作用是寻找元素x的代表元素
        if self.parent[x]!=x:
            # 注意，在递归地寻找父元素时，每一步操作并不浪费。
            # 我们递归地把跨越两层的路径压缩成跨越1层路径，这样能有效减少后续递归层数。
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        # 找到各自元素的代表元素
        root_x=self.find(x)
        root_y=self.find(y)
        # 如果代表元素相同，说明属于一个集合，两元素无需合并
        if root_x==root_y:
            return
        # 如果一个的秩更大，那么把另一个元素挂到他的下面
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
        # 如果秩一样大，那么把一个合并到另一个后，根的秩要+1
        else:
            self.parent[root_y]=root_x
            self.rank[root_x]+=1

num=1
while True:
    root_set=set()
    n,m=map(int,input().split())
    if n==0 and m==0:break
    DJS=DisjointSet(n)

    for _ in range(m):
        i,j=map(int,input().split())
        DJS.union(i,j)

    for i in range(1,n+1):
        root_set.add(DJS.find(i))

    print("Case {}: {}".format(num,len(root_set)))
    num+=1