def queen_stack(n):
    res,stack=[],[]
    stack.append((0,[]))
    while stack:
        row,cols=stack.pop()
        if row==n:
            res.append(cols)
        else:
            for col in range(n):
                if is_valid(row,col,cols):
                    stack.append((row+1,cols+[col]))
    return res

def is_valid(row,col,cols):
    for i,j in enumerate(cols):
        # i表示已占用行，j表示已占用列
        if i==row or j==col:return False
        if abs(i-row)==abs(j-col):return False
    return True

res,Q=queen_stack(8),[]

for i in res:
    tmp=[str(1+j) for j in i]
    Q.append(int("".join(tmp)))

for i in Q:print(i)