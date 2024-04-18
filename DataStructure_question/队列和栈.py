from collections import deque
for _ in range(int(input())):
    queue, stack = deque(), list()
    # 每一轮初始化状态为True
    q_flag=s_flag=1

    for i in range(int(input())):
        a=input()
        if a=="pop":
            op="pop"
            # 如果过程中操作出现错误，标记为False
            try:queue.popleft()
            except:q_flag=0
            try:stack.pop()
            except:s_flag=0
        else:
            op,num=map(str,a.split())
            if q_flag!=0:
                queue.append(int(num))
            if s_flag!=0:
                stack.append(int(num))
    # 统一输出答案，只输出一次
    if q_flag:print(*queue)
    else:print("error")
    if s_flag:print(*stack)
    else:print("error")