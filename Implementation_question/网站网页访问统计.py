def time_shift(s:str):
    hour,min,sec = s.split(':')
    time=60*60*int(hour)+60*int(min)+int(sec)
    return time

from collections import defaultdict
webs=defaultdict(int)
for _ in range(int(input())):
    web,start,end=map(str,input().split())
    span=time_shift(end)-time_shift(start)
    webs[web]+=span

compare,ans=0,None
for web,span in webs.items():
    if span>compare:
        compare=span
        ans=web

print(ans)
