d=[(-1,-2),(-2,-1),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
res=0
def dfs(X,Y,path,start):
    global res
    if path==X*Y:
        res+=1
        return

    x, y = start
    for dx,dy in d:
        if 0<=x+dx<X and 0<=y+dy<Y and not visited[x+dx][y+dy]:
            visited[x+dx][y+dy]=True
            dfs(X,Y,path+1,(x+dx,y+dy))
            visited[x+dx][y+dy]=False

for i in range(T:=int(input())):
    X,Y,x,y=map(int,input().split())
    res=0
    visited=[[False for j in range(Y)] for i in range(X)]
    visited[x][y]=True
    dfs(X,Y,1,(x,y))
    print(res)