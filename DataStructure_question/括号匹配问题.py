"""
模拟问题，先倒序找最右边的左括号，并向右匹配最近的右括号；
匹配后修改，当找不到左括号时，剩下的右括号必然无法匹配
"""
while True:
    try:
        raw=list(input())
        lst_idx,lst_val=[],[]
        for idx,val in enumerate(raw):
            if val=="(" or val==")":
                lst_val.append(val)
                lst_idx.append(idx)
        # print(lst_val,lst_idx)
        while True:
            temp_l=None
            for i in range(len(lst_val)-1,-1,-1):
                if lst_val[i]=="(":
                    temp_l=i
                    break
            if temp_l==None:
                break
            tmp_val=lst_val[temp_l:]
            if ")" not in tmp_val:
                lst_val[temp_l] = "$"
            else:
                temp_r=tmp_val.index(")")
                tmp_val[0]=" "
                tmp_val[temp_r]=" "
                lst_val=lst_val[:temp_l]+tmp_val
        for i in range(len(lst_val)):
            if lst_val[i]==")":
                lst_val[i]="?"
        res=[" "]*len(raw)
        for idx,val in zip(lst_idx,lst_val):
            res[idx]=val
        print("".join(raw))
        print("".join(res))
    except EOFError:
        break