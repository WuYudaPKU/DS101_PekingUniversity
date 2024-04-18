while True:
    n=int(input())
    if n==0:
        break
    hotels=[tuple(map(int,input().split())) for _ in range(n)]
    hotels.sort(key=lambda x:(x[0],x[1]))
    res=1
    pre_max=hotels[0][1]
    for i in range(n):
        if hotels[i][1]<pre_max:
            res+=1
            pre_max=hotels[i][1]
    print(res)