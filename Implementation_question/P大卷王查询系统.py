def is_PKUBadGuy(lst):
    global x,y
    if sum(lst)/len(lst)>y and len(lst)>=x:return True
    else:return False

from collections import defaultdict
n,x,y=map(int,input().split())
sys=defaultdict(list)
for i in range(n):
    c,p,s=map(str,input().split())
    sys[p].append(int(s))
for _ in range(int(input())):
    if is_PKUBadGuy(sys[input()]):print("yes")
    else:print("no")