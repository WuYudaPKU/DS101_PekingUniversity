import heapq
res=[]
n,k=map(int,input().split())
raw,heap=tuple(map(int,input().split())),[]

if n>k:
    # 前k个元素入堆
    for i in range(k):
        heapq.heappush(heap,(-raw[i],i))

    # 滑动窗口遍历闭区间[i,i+k]的所有元素
    for i in range(0,n-k+1):
        # 如果弹出元素的索引小于i，舍弃；
        while (tmp:=heapq.heappop(heap))[1]<i:
            continue
        res.append(-tmp[0])
        # 不确定弹出元素是否还有用，再次入堆
        heapq.heappush(heap,tmp)
        # 末尾索引越界，添加最后一次边界条件
        if i+k<=len(raw)-1:
            heapq.heappush(heap,(-raw[i+k],i+k))
# 不用滑动的情况
elif n==k:
    res.append(max(raw))

print(*res)
