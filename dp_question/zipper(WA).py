def is_zipper(a:str,b:str,c:str):
    # 三指针
    _p,_p1,_p2=0,0,0
    while _p1<len(a) and _p2<len(b):
        if a[_p1]==c[_p]:
            _p1+=1
            _p+=1
            continue
        if b[_p2]==c[_p]:
            _p2+=1
            _p+=1
            continue
        _p1+=1
        _p2+=1

    if _p1>=len(a):
        while _p2<len(b):
            if b[_p2] == c[_p]:
                _p2+=1
                _p+=1
                continue
            _p2+=1

    if _p2>=len(b):
        while _p1<len(a):
            if a[_p1] == c[_p]:
                _p1+=1
                _p+=1
                continue
            _p1+=1
    if _p==len(c):return "yes"
    else:return "no"

for i in range(int(input())):
    a,b,c=map(str,input().split())
    print("Data set {}: {}".format(i+1,is_zipper(a,b,c)))
