from collections import defaultdict
raw=list(map(int,input().split()))
votes=defaultdict(int)
for i in raw:
    votes[i]+=1

temp=[(i,j) for i,j in votes.items()]
temp.sort(key=lambda x:x[1],reverse=True)

out=[]
for i in temp:
    if i[1]==max(votes.values()):
        out.append(i[0])
    else:
        break
out.sort()
print(*out)