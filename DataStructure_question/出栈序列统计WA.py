def dfs_stack_out(stack,wait,path,n):
    # 函数的功能是对于当前stack和wait，在结果里加入所有可能的序列
    # 在一轮递归中，可以执行以下2种操作：
    # 1. stack进元素
    # 2. stack出元素
    global res
    # 边界条件
    if len(path) == n:
        res.append(path)
        return
    #只进元素
    if wait:
        to_in=wait.pop()
        stack.append(to_in)
        dfs_stack_out(stack,wait,path,n)
        # 回溯
        stack.pop()
        wait.append(to_in)

    # 只出元素
    if stack:
        out=stack.pop()
        path+=out
        dfs_stack_out(stack,wait,path,n)
        # 回溯
        stack.append(out)
    return


res=[]
n=int(input())
dfs_stack_out([],[str(i) for i in range(n)],"",n)
print(len(res))