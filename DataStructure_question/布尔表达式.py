# 中缀转后缀
def ShuntingYard(l:list):
    stack,output=[],[]
    for i in l:
        if i==" ":continue
        if i in 'VF':output.append(i)
        elif i=='(':stack.append(i)
        elif i in '&|!':
            while True:
                if i=='!':break
                elif not stack:break
                elif stack[-1]=="(":
                    break
                else:output.append(stack.pop())
            stack.append(i)
        elif i==')':
            while stack[-1]!='(':
                output.append(stack.pop())
            stack.pop()
    if stack:output.extend(reversed(stack))
    return output

# 简洁地转化字符串和布尔类型
def Bool_shift(a):
    if a=='V':return True
    elif a=='F':return False
    elif a==True:return 'V'
    elif a==False:return 'F'

# 定义计算操作
def cal(a,operate,b=None):
    if operate=="&":return Bool_shift(Bool_shift(a) and Bool_shift(b))
    if operate=="|":return Bool_shift(Bool_shift(a) or Bool_shift(b))
    if operate=="!":return Bool_shift(not Bool_shift(a))

# 计算后续表达式
def post_cal(l:list):
    stack=[]
    for i in l:
        if i in 'VF':stack.append(i)
        elif i in "&|!":
            if i=="!":
                stack.append(cal(stack.pop(),'!'))
            else:
                a,b=stack.pop(),stack.pop()
                stack.append(cal(a,i,b))
    return stack[0]

while True:
    try:print(post_cal(ShuntingYard(list(input()))))
    except EOFError:break