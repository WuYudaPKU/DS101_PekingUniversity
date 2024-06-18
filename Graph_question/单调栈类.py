# 默认为非严格单调递增栈
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
    def push(self, item):
        while self.stack and self._compare(self.stack[-1],item)==self.increasing:
            self.stack.pop()
        self.stack.append(item)
    def _compare(self,a,b):
        if a>b:return True
        else:return False


stack=MonotonicStack()
while True:
    tmp=int(input())
    stack.push(tmp)
    print(stack)