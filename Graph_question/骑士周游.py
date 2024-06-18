d=[(-1,-2),(-2,-1),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
def avail(vert):
    x,y=vert
    return (0 <=x<X and 0<=y<Y and not visited[x][y])

def ordered_by_avail(start):
    x,y=start
    steps=[]
    for dx,dy in d:
        next_step=(x+dx,x+dy)
        available=0
        for step in d:
            ddx,ddy=step
            if avail((x+dx+ddx,y+dy+ddy)):
                available+=1
        steps.append((available,(dx,dy)))
    steps.sort(key=lambda x:x[0])
    return [i[1] for i in steps]

def dfs(X,Y,path,start):
    if path==X*Y:
        print('success')
        exit()
    x, y = start
    new_d=ordered_by_avail(start)
    for dx,dy in new_d:
        if avail((x+dx,y+dy)):
            visited[x+dx][y+dy]=True
            dfs(X,Y,path+1,(x+dx,y+dy))
            visited[x+dx][y+dy]=False

X=Y=int(input())
x,y=map(int,input().split())
visited=[[False for j in range(Y)] for i in range(X)]
visited[x][y]=True
dfs(X,Y,1,(x,y))
print('fail')