l=[]
while True:
    p,e,i,d=map(int,input().split())
    if p == -1: break
    l.append((p,e,i,d))


def Calculate(p,e,i,d):
    t=0
    for j in range(max(p,e,i,d),42505):
        if (j-p)%23==(j-e)%28==(j-i)%33==0:
            t=j
            break
    if t-d==0:return 21252
    return t-d

flag=1
for p,e,i,d in l:
    print('Case {}: the next triple peak occurs in {} days.'.format(flag,(Calculate(p,e,i,d))))
    flag+=1