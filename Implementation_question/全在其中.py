def judge(s:str,t:str):
    _p1,_p2=0,0
    while _p1<len(s) and _p2<len(t):
        if s[_p1]==t[_p2]:
            _p1+=1
            _p2+=1
        else:
            _p2+=1
    return _p1==len(s)

while True:
    try:
        s,t=map(str,input().split())
        print("Yes" if judge(s,t) else "No")
    except EOFError:break