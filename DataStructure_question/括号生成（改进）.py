# 使用dfs实现
res=[]
def dfs_brackets(n,path:str,lefts:int,rights:int):
    global res
    # 边界条件
    if len(path)==n*2:
        res.append(path)
        return
    # 递归
    for i in '()':
        if i=='(':
            if lefts<n:
                dfs_brackets(n,path+i,lefts+1,rights)
        else:
            # 利用条件剪枝
            if rights<lefts and rights<n:
                dfs_brackets(n,path+i,lefts,rights+1)
    return

dfs_brackets(int(input()),"",0,0)
for i in res:print(i)