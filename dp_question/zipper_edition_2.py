# dp[i][j]表示a的前i部分和b的前j部分能否组成c的前i+j部分。
for _ in range(n:=int(input())):
    a,b,c=map(str,input().split())
    # 添加占位符让dp公式简明。
    a,b,c="@"+a,"@"+b,"@"+c

    # 初始化dp表
    dp=[[None for _ in range(len(b))] for _ in range(len(a))]
    # 根据实际意义赋初值
    dp[0][0]=True
    for i in range(1,len(a)):
        dp[i][0]=(a[:i]==c[:i])
    for j in range(1,len(b)):
        dp[0][j]=(b[:j]==c[:j])

    # dp过程
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            dp[i][j]=(dp[i-1][j] and a[i]==c[i+j]) or (dp[i][j-1] and b[j]==c[i+j])

    if dp[-1][-1]:print('Data set {}: yes'.format(_+1))
    else:print('Data set {}: no'.format(_+1))
