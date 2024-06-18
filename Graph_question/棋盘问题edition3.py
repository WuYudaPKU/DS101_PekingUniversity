n,k,res=0,0,0
chess=[[0 for _ in range(10)] for _ in range(10)]
col_visited=[False for _ in range(10)]
def ChessBoard(current_row,taken_nums):
    global n,k,col_visited,chess,res
    if taken_nums==k:
        res+=1
        return
    if current_row==n+1:
        return

    for i in range(current_row,n):
        for j in range(n):
            if not col_visited[j] and chess[i][j]=='#':
                col_visited[j]=True
                ChessBoard(i+1,taken_nums+1)
                col_visited[j]=False
    return

while (t:=input())!='-1 -1':
    n,k=map(int,t.split())
    for i in range(n):
        chess[i]=list(input())
    res,col_visited=0,[False for _ in range(10)]
    ChessBoard(0,0)
    print(res)