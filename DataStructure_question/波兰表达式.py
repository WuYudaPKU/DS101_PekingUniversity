def cal(x1,x2,operate):
    m,n=float(x1),float(x2)
    if operate=="+":return m+n
    if operate=="-":return m-n
    if operate=="*":return m*n
    if operate=="/":return m/n
#用一个空栈存放数字，遇到数字则入栈，
#遇到运算符则弹出两个数字执行运算。
    
raw,stack=list(map(str,input().split())),[]
operators=["+","-","*","/"]
for i in range(len(raw)-1,-1,-1):
    if raw[i] not in operators:stack.append(raw[i])
    else:stack.append(cal(stack.pop(),stack.pop(),raw[i]))
print("{:.6f}".format(stack[-1]))