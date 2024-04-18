raw=list(map(str,input().split()))
stack=[]
while raw:
    stack.append(raw.pop())
print(' '.join(stack))