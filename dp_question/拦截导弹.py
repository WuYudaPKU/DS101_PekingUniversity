import math
n,res=int(input()),0
def dfs(path,now,left):
    global res
    if len(left)==0:
        res=max(res,len(path))
        return
    for i in range(len(left)):
        if left[i]>now:
            continue
        dfs(path+[i],left[i],left[i+1:])
    return

dfs([],math.inf,list(map(int,input().split())))
print(res)