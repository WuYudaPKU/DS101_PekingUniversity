# 默认为非严格单调递增栈
n,raw=int(input()),[0]+list(map(int,input().split()))
ans,stack=[0 for _ in range(n+1)],[]
for i in range(n,-1,-1):
    while stack and raw[stack[-1]]<=raw[i]:
        stack.pop()
    if stack:ans[i]=stack[-1]
    stack.append(i)
print(*ans[1:])