from collections import defaultdict
d=defaultdict(list)

for _ in range(int(input())):
    n,m,date=map(str,input().split())
    d[(int(m),int(date))].append(n)
lst=[(key,tuple(value)) for key,value in d.items()]
lst.sort(key=lambda x:(x[0][0],x[0][1]))

for i in lst:
    if len(i[1])>1:
        print(i[0][0],i[0][1],*i[1])