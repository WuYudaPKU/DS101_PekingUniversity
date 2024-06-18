from math import inf
class MonotonicStack:
    def __init__(self, increasing=True):
        # increasing表示从栈底到栈顶是单调递增的
        self.increasing = increasing
        self.stack=[]
    def __str__(self):
        return str(self.stack)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def top(self):
        return self.stack[-1] if self.stack else None
    def clear(self, item):
        while self.stack and self._compare(self.stack[-1],item)==self.increasing:
            self.stack.pop()
    def _compare(self,a,b):
        if b<a or b==a:return True
        else:return False

class Cow:
    def __init__(self,idx,height):
        self.idx=idx
        self.height=height
    def __lt__(self,other):
        return self.height<other.height
    def __eq__(self,other):
        return self.height==other.height
    def __str__(self):
        return str((self.idx,self.height))

N,cows=int(input()),[Cow(0,inf)]
hi=[int(input()) for _ in range(N)]
for idx,height in enumerate(hi):
    cows.append(Cow(idx+1,height))
cows.append(Cow(N+1,-inf))

stack_1=MonotonicStack(increasing=True)
next_less=[N+1 for _ in range(N+2)]
for idx in range(N+1,-1,-1):
    cur_cow=cows[idx]
    if stack_1.top() is None:
        stack_1.stack.append(cur_cow)
    else:
        if stack_1.top()<cur_cow:
            next_less[idx]=stack_1.top().idx
            stack_1.stack.append(cur_cow)
        else:
            stack_1.clear(cur_cow)
            if stack_1.stack:
                next_less[idx]=stack_1.top().idx
            stack_1.stack.append(cur_cow)

stack_2=MonotonicStack(increasing=False)
pre_greater=[0 for _ in range(N+2)]
for idx in range(N+1):
    cur_cow=cows[idx]
    if stack_2.top() is None:
        stack_2.stack.append(cur_cow)
    else:
        if cur_cow<stack_2.top():
            pre_greater[idx]=stack_2.top().idx
            stack_2.stack.append(cur_cow)
        else:
            stack_2.clear(cur_cow)
            if stack_2.stack:
                pre_greater[idx]=stack_2.top().idx
            stack_2.stack.append(cur_cow)

res=0
for i in range(N+1,-1,-1):
    for j in range(1,i):
        if (pre_greater[i]<j and next_less[j]>i):
            res=i-j+1
            break

print(pre_greater,next_less)
print(res)