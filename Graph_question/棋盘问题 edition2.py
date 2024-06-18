res=0
def DFS_ChessBoard(n,k,matrix,path:list,row:list,col:list,p,q):
    global res,visited
    

while (t:=input())!='-1 -1':
    n,k=map(int,t.split())
    visited=[[False for i in range(n)] for j in range(n)]
    res,matrix=0,[]
    for i in range(n):
        matrix.append(list(input()))
    DFS_ChessBoard(n,k,matrix,[],[],[])
    print(res)