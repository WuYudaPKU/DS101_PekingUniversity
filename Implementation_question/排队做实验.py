n,res,wait=int(input()),[],0
time=[0]+list(map(int,input().split()))
t_time=list((time[i],i) for i in range(1,n+1))
t_time.sort()
# print(t_time)
for i in range(n):
    res.append(t_time[i][1])
    wait+=t_time[i][0]*(n-1-i)
print(*res)
print('{:.2f}'.format(wait/n))