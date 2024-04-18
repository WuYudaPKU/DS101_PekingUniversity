while True:
    try:
        raw,stack,res=list(input()),[],[]
        for i in range(len(raw)):
            if raw[i]==")":
                if stack:
                    tmp=stack.pop()
                    res[tmp[0]]=" "
                    res.append(" ")
                else:
                    res.append("?")
            elif raw[i]=="(":
                stack.append((i,"("))
                res.append("$")
            else:res.append(" ")
        print("".join(raw)+"\n"+"".join(res))
    except EOFError:break