def A_over_B(A,B):
    if B=="(": return True
    if A=='*' or '/': return True
    if (A=='*' or A=="/") and (B=='+' or B=='-'):
        return True
    return False

operators_1=['+','-','*','/','(',')']

def pre_to_post(lst):
    operators,output=[],[]
    while lst:
        tmp=lst.pop(0)
        if not operators:
            operators.append(tmp)
            continue
        if tmp not in operators_1:
            output.append(tmp)
        else:
            if tmp==")":
                if output[-1] not in operators_1 and operators[-1]=="(":
                    continue
                else:
                    output.append(operators.pop())
            else:
                if A_over_B(tmp,a:=operators.pop()):
                    operators.append(a)
                    operators.append(tmp)
                else:
                    output.append(tmp)
        while "(" in output:
            output.remove("(")
    for i in range(len(operators)-1,-1,-1):
        if operators[i]!="(":
            output.append(operators[i])
    return output

for _ in range(int(input())):
    a=pre_to_post(list(map(str,input().split())))
    print(*a)
# ( 3 ) * ( ( 3 + 4 ) * ( 2 + 3.5 ) / ( 4 + 5 ) )